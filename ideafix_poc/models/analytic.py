# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID

class AnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    start_longitude = fields.Char(string="Start Longitude")
    start_latitude = fields.Char(string="Start Latitude")
    end_longitude = fields.Char(string="End Longitude")
    end_latitude = fields.Char(string="End Latitude")