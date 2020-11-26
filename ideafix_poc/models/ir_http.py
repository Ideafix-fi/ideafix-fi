# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models
from odoo.http import request


class Http(models.AbstractModel):
    # Private attributes
    _inherit = 'ir.http'

    # Business methods
    # -----------------
    def session_info(self):
        result = super(Http, self).session_info()
        result['font_selection'] = request.session.uid and self.env.user.font_selection
        return result
