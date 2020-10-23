odoo.define('fsm.geolocation', function(require) {
    "use strict";

    var core = require('web.core');
    var widgetRegistry = require('web.widget_registry');
    var Widget = require('web.Widget');
    var Class = require("web.Class");
    var framework = require('web.framework');

    var _t = core._t;

    var FsmGeolocationWidget = Widget.extend({
        template: 'FsmGeolocationWidget',
        events: {
            'click': '_onClickStart',
        },

        init: function (parent, record, nodeInfo) {
            this._super.apply(this, arguments);
            this.res_id = record.res_id;
            this.res_model = record.model;
            this.state = record;
            this.node = nodeInfo;
            this.coords = {lat: false, long: false};
        },
        start: function() {
            this._super.apply(this, arguments);
        },
        /**
         * Geolocate
         * @private
         */
        _geolocate: function () {
            var self = this;
            if (navigator.geolocation) {
                return new Promise(function(resolve, reject) {
                    navigator.geolocation.getCurrentPosition(resolve, reject);
                });
            }
            return Promise.resolve({})
        },
        _onClickStart: async function (data) {
            var self = this;
            if (self.node.attrs.action) {
                var coords = {lat: false, long: false};
                var position = await this._geolocate();
                if (position) {
                    coords.lat = position.coords.latitude;
                    coords.long = position.coords.longitude;
                }
                const res = await self._rpc({
                    model: self.res_model,
                    method: self.node.attrs.action,
                    args: [self.res_id],
                    kwargs: {
                        'lat': coords.lat, 'long': coords.long},
                });
                if (res) {
                    self.do_action(res, {
                        on_close: function() {self.trigger_up('reload');},
                    });
                } else {
                    self.trigger_up('reload');
                }
            }
        }
    });

    widgetRegistry.add('fsm_geolocation', FsmGeolocationWidget);

});