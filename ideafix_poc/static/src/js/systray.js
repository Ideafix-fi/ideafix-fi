odoo.define('ideafix.systray', function (require) {
    "use strict";
    
    require('mail.systray.ActivityMenu');
    var SystrayMenu = require('web.SystrayMenu');
    var session = require('web.session');
    var Widget = require('web.Widget');
    var config = require('web.config');
    var font_size_selector = '.o_form_sheet td label, .o_form_sheet td, .o_kanban_view, .o_form_sheet .o_notebook';
    var SIZE_MAP = {
        original: '13px',
        medium: '15px',
        large: '18px',
    }

    var FontSizeWidget = Widget.extend({
        template:'FontSizeWidget',
        events: {
            'click .dropdown-menu.font_size li a[data-menu]': '_onClickFontSize'
        },
    
        init: function() {
            this.selected_size = 'original';
            this._super.apply(this, arguments);
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
            self.$('.oe_topbar_name').text(this.selected_size);
            this._updateFontSize();
        },
        _updateFontSize: function() {
            $(font_size_selector).css('font-size', SIZE_MAP[this.selected_size]);
        }
    
    });
    console.log('>>>>>', session)
    SystrayMenu.Items.push(FontSizeWidget);

    // if (config.device.isMobile) {
    // }
});