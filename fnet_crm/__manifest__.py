# -*- coding: utf-8 -*-
{
    'name': "fnet_crm",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Futurenet Technology",
    'website': "http://www.futurenet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','sale','voip','purchase','calendar','sale_crm',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/ir.sequence.xml',
        'views/views.xml',
        # 'report/report_budget.xml',
        # 'security/security.xml',
        # 'security/ir.model.access.xml',
        # 'security/ir.model.access.xml',
        # # 'views/crm_inherit_view.xml',
        # 'views/templates.xml',
        # 'views/oppor_orderline_view.xml',
        # 'views/oppor_sequence.xml',
        # 'views/product_view.xml',
        # 'views/purchase_draft_sequence.xml',
        # 'views/purchase_order_sequence.xml',
        # 'views/purchase_requisition_view.xml',
        # 'views/purchase_view.xml',
        # 'views/sale_amendment_sequence.xml',
        # 'views/sale_config_setting_view.xml',
        # 'views/sale_order_sequence.xml',
        # 'views/sale_team_view.xml',
        # 'views/sale_view.xml',
    ],
'qweb': [
        "static/xml/sales_team_dashboard.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
