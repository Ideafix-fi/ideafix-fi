# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProjectTaskCreateTimesheet(models.TransientModel):
    _inherit = 'project.task.create.timesheet'

    end_longitude = fields.Char(string="End Longitude")
    end_latitude = fields.Char(string="End Latitude")

    def save_timesheet(self):
        result = super(ProjectTaskCreateTimesheet, self).save_timesheet()
        task_id = self.env['project.task'].browse(self._context.get('active_id'))
        result.write({
            'start_latitude': task_id.start_latitude,
            'start_longitude': task_id.start_longitude,
            'end_latitude': self.end_latitude,
            'end_longitude': self.end_longitude,
            })
        return result
