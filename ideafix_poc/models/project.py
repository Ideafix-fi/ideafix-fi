# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _inherit = 'project.task'

    task_stage_id = fields.Many2one('task.status.stage',
        string='Tracking Stage',
        copy=False
    )

    start_longitude = fields.Char(string="Start Longitude")
    start_latitude = fields.Char(string="Start Latitude")

    def _compute_access_url(self):
        super(Task, self)._compute_access_url()
        for task in self:
            task.access_url = '/my/task/track/%s' % (task.id)

    def action_start(self, lat=False, long=False):
        self.ensure_one()
        if lat and long:
            self.write({'start_longitude': long, 'start_latitude': lat})
        self.action_timer_start()
        return False

    def action_stop(self, lat=False, long=False):
        self.ensure_one()
        if lat and long:
            self.write({'start_longitude': long, 'start_latitude': lat})
        res = self.action_timer_stop()
        if res:
            res['context']['default_end_latitude'] = lat
            res['context']['default_end_longitude'] = long
        return res

    @api.model
    def create(self, vals):
        res = super(Task, self).create(vals)
        res._send_status_tracking_mail()
        return res

    def _send_status_tracking_mail(self):
        template = self.env.ref('ideafix_poc.mail_template_project_task_stage_status', False)
        if template:
            template.send_mail(self.id)