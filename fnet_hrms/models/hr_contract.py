
from odoo import models, fields, api


class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = "HrContract"

    # active = fields.Boolean('Active',default=True)
    is_hra = fields.Boolean(string='Is HRA',default=False)
    is_pt = fields.Boolean(string='Is PT',default=False)
    is_bonus = fields.Boolean(string='Is Bonus',default=False)
    is_medical = fields.Boolean(string='Is Medical',default=False)
    is_convayance = fields.Boolean(string='Is convayance',default=False)
    is_travel_added = fields.Boolean(string='Is TA Not in Basic',default=False)
    is_other = fields.Boolean(string='Is Other Allownace',default=False)
    is_resigned = fields.Boolean(string='Is Resigned',default=False)
    is_arrear = fields.Boolean(string='Is salary Revised',default=False)
    pt = fields.Float(string='PT', digits=(16, 5))
    medical = fields.Float(string='Medical', digits=(16, 5))
    convanyance = fields.Float(string='Conveyance', digits=(16, 5))
    other = fields.Float(string='Other Allownace',digits=(16, 5))
    hra = fields.Float(string='HRA', digits=(16, 5))
    bonus = fields.Float(string='Bonus', digits=(16, 5))
    effective_date = fields.Date(string='Effective Date',readonly=True)
    # history_line = fields.One2many('salary.history.line','contract_id','Salary History')
    salary_arrear = fields.Float(string='Salary Arrear', digits=(16, 5),readonly=False)
    learning_development = fields.Float(string='Learning and Development', digits=(16, 5))
    tds_deduction = fields.Float(string='TDS',default=False)
    mobile_deduction = fields.Float(string='Mobile Deduction',default=False)
    other_deduction = fields.Float(string='Other Deduction',default=False)
    salary_advance = fields.Float(string='Salary Advance',default=False)
    arrears = fields.Float(string='Arrear ',default=False)
    is_esi = fields.Boolean(string='IS ESI ',default=False)
    # trail_date_start = fields.Date(String='Trail Period Duration')
    duration = fields.Date(string="Duration")
    working_hours = fields.Many2one(string='Working Schedule')
    schedule_pay = fields.Selection([('monthly','Monthly'),('quarterly','Quarterly'),('semi-annually','Semi-Annually'),('annually','Annually'),('weekly','Weekly'),('bi-weekly','Bi-Weekly'),('bi-monthly','Bi-Monthly')], String = 'Schedule Pay',readonly=True)
    consolidate = fields.Char(string='Consolidate Pay')
    basic_percentage = fields.Float(string='Basic Percentage')
    trance_allowance = fields.Float(string='Trance Allowance')
    ea_allowance = fields.Float(string='EA Allowance')
    data_card_allowance = fields.Float(string='Data Card Allowance')
    ot_allowance = fields.Float(string='OT Allowance')


