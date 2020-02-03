
from odoo import models, fields, api


class HrContract(models.Model):
    _inherit = 'hr.contract'

    # active = fields.Boolean('Active',default=True)
    is_hra = fields.Boolean(String='Is HRA',default=False)
    is_pt = fields.Boolean(String='Is PT',default=False)
    is_bonus = fields.Boolean(String='Is Bonus',default=False)
    is_medical = fields.Boolean(String='Is Medical',default=False)
    is_convayance = fields.Boolean(String='Is convayance',default=False)
    is_travel_added = fields.Boolean(String='Is TA Not in Basic',default=False)
    is_other = fields.Boolean(String='Is Other Allownace',default=False)
    is_resigned = fields.Boolean(String='Is Resigned',default=False)
    is_arrear = fields.Boolean(String='Is salary Revised',default=False)
    pt = fields.Float(String='PT', digits=(16, 5))
    medical = fields.Float(String='Medical', digits=(16, 5))
    convanyance = fields.Float(String='Conveyance', digits=(16, 5))
    other = fields.Float(String='Other Allownace',digits=(16, 5))
    hra = fields.Float(String='HRA', digits=(16, 5))
    bonus = fields.Float(String='Bonus', digits=(16, 5))
    effective_date = fields.Date(String='Effective Date',readonly=True)
    # history_line = fields.One2many('salary.history.line','contract_id','Salary History')
    salary_arrear = fields.Float(String='Salary Arrear', digits=(16, 5),readonly=False)
    learning_development = fields.Float(String='Learning and Development', digits=(16, 5))
    tds_deduction = fields.Float(String='TDS',default=False)
    mobile_deduction = fields.Float(String='Mobile Deduction',default=False)
    other_deduction = fields.Float(String='Other Deduction',default=False)
    salary_advance = fields.Float(String='Salary Advance',default=False)
    arrears = fields.Float(String='Arrear ',default=False)
    is_esi = fields.Boolean(String='IS ESI ',default=False)
    # trail_date_start = fields.Date(String='Trail Period Duration')
    duration = fields.Date(String="Duration")
    working_hours = fields.Many2one(String='Working Schedule')
    schedule_pay = fields.Selection([('monthly','Monthly'),('quarterly','Quarterly'),('semi-annually','Semi-Annually'),('annually','Annually'),('weekly','Weekly'),('bi-weekly','Bi-Weekly'),('bi-monthly','Bi-Monthly')], String = 'Schedule Pay',readonly=True)
    consolidate = fields.Char(String='Consolidate Pay')
    basic_percentage = fields.Float(String='Basic Percentage')
    trance_allowance = fields.Float(String='Trance Allowance')
    ea_allowance = fields.Float(String='EA Allowance')
    data_card_allowance = fields.Float(String='Data Card Allowance')
    ot_allowance = fields.Float(String='OT Allowance')


