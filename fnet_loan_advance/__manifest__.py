# -*- coding: utf-8 -*-
{
    'name': "Futurenet Loan/ Salary Advance",

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
    'depends': ['base', 'hr', 'hr_payroll'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_loan_seq.xml',
        'data/hr_contract_type_data.xml',
        'data/salary_rule_loan.xml',
        'views/hr_loan_views.xml',
        'views/contract_view.xml',
        'views/hr_payroll_views.xml',
    ],
}
