# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TaskStatusStage(models.Model):
    _name = 'task.status.stage'
    _description = 'Task Status Stages'

    name = fields.Char(string='Name', required=True, translate=True)
