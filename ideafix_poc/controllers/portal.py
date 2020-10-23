# -*- coding: utf-8 -*-
from odoo import http

from odoo.http import request
from odoo.exceptions import AccessError, MissingError

from odoo.addons.portal.controllers.portal import CustomerPortal


class IdeafixCustomerPortal(CustomerPortal):
    @http.route(['/my/task/track/<int:task_id>'], type='http', auth="public", website=True)
    def portal_task_track_page(self, task_id, access_token=None, **kw):
        try:
            task_sudo = self._document_check_access('project.task', task_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')
        return request.render('ideafix_poc.task_trace_page', {'task': task_sudo})