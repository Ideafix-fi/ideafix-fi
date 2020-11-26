# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResUsers(models.Model):
    # Private attributes
    _inherit = 'res.users'

    # ------------
    # Fields Declaration
    # ------------
    font_selection = fields.Selection([('original', 'Original'), ('medium', 'Medium'), ('large', 'Large')], default='original', string='Font Size')

    # model method
    def __init__(self, pool, cr):

        init_res = super(ResUsers, self).__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(['font_selection'])
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(['font_selection'])
        return init_res
