# -*- coding: utf-8 -*-
{
    'name': "fnet_crm_sequence",

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
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','crm','base','sale_crm','purchase_requisition','purchase',],

    # always loaded
    'data': [

        'views/oppor_sequence.xml',
        'views/purchase_order_sequence.xml',
        'views/sale_order_sequence.xml',
        'views/sale_amendment_sequence.xml',

            ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
