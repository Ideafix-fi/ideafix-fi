# -*- coding: utf-8 -*-
{
    'name': "project_and_field_customization",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['industry_fsm','website','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'data/mail_data.xml',

        'views/project_view.xml',
        'views/project_stage_view.xml',
        'views/templates.xml',
        'views/analytic_view.xml',

        'wizard/project_task_create_timesheet_views.xml',
    ],
    'qweb': [
        'static/src/xml/fsm.xml',
    ],

}
