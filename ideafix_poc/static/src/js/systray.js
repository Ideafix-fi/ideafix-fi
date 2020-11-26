odoo.define('ideafix.systray', function (require) {
    "use strict";
    
    require('mail.systray.ActivityMenu');
    var SystrayMenu = require('web.SystrayMenu');
    var session = require('web.session');
    var Widget = require('web.Widget');
    var config = require('web.config');
    var FormRenderer = require('web.FormRenderer');


    FormRenderer.include({
        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                if (_.contains(['medium', 'large'], session.font_selection))
                    self.$el.addClass(session.font_selection)
            });
        },
    })

    var FontSizeWidget = Widget.extend({
        template:'FontSizeWidget',
        events: {
            'click .dropdown-menu.font_size li a[data-menu]': '_onClickFontSize'
        },
    
        init: function() {
            this.selected_size = 'original';
            this._super.apply(this, arguments);
        },
        willStart: function () {
            var self = this;
            return this._rpc({
                model: 'res.users',
                method: 'read',
                args: [[session.uid], ['font_selection']],
            }).then(function (user) {
                self.selected_size = user && user[0].font_selection;
            })
        },
        start: function() {
            this.$('.oe_topbar_name').text(this.selected_size);
            this._super();
        },
        _onClickFontSize: function(ev) {
            var self = this;
            ev.preventDefault();
            var selected_size = $(ev.currentTarget).data('size');
            this.selected_size = selected_size;
            self._rpc({
                model: 'res.users',
                method: 'write',
                args: [[session.uid], {'font_selection': selected_size}],
            }).then(function () {
                self.$('.oe_topbar_name').text(self.selected_size);
                location.reload();
            });
        },
    
    });

    if (config.device.isMobile) {
        SystrayMenu.Items.push(FontSizeWidget);
    }
});