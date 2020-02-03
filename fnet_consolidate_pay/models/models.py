from odoo import api, fields, models


class ConsolidatePay(models.Model):
    _inherit = 'hr.contract'

    consolidate_pay = fields.Float('Total Consolidate Pay', compute='_consolidate')
    total_consolidate = fields.Float('Consolidate Pay')

    def _consolidate(self):
        addition = self.basics_percentage or 0 + self.trans_allowance or 0 + self.ea_allowance or 0 + self.data_card__allowance or 0 + self.overtime__allowance or 0 + self.new_employee or 0 + self.learning_development or 0 + self.pt or 0 + self.hra or 0 + self.bonus or 0 + self.medical or 0 + self.convenyance or 0 + self.other or 0
        deduction = self.tedious_deduction or 0 + self.other_deduction or 0 + self.arrears or 0 + self.mobile_deduction or 0 + self.salary_advance or 0 + self.salary_arrear or 0
        self.consolidate_pay = addition - deduction
