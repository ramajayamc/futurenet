# -*- coding: utf-8 -*-
import time as time_1
import babel
from datetime import date, datetime, time, timedelta
from odoo import models, fields, api, tools, _
from pytz import timezone, utc
from collections import defaultdict
from odoo.tools import float_utils
from odoo.exceptions import UserError, ValidationError
ROUNDING_FACTOR = 16


class HrPayslipInput(models.Model):
    _inherit = 'hr.payslip.input'

    loan_line_id = fields.Many2one('hr.loan.line', string="Loan Installment")


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.model
    def get_worked_day_lines(self, contracts, date_from, date_to):
        """
        @param contract: Browse record of contracts
        @return: returns a list of dict containing the input that should be applied for the given contract between date_from and date_to
        """
        res = []
        # fill only if the contract as a working schedule linked
        for contract in contracts.filtered(lambda contract: contract.resource_calendar_id):
            day_from = datetime.combine(fields.Date.from_string(date_from), time.min)
            day_to = datetime.combine(fields.Date.from_string(date_to), time.max)

            # compute leave days
            leaves = {}
            calendar = contract.resource_calendar_id
            tz = timezone(calendar.tz)
            day_leave_intervals = contract.employee_id.list_leaves(day_from, day_to, calendar=contract.resource_calendar_id)
            for day, hours, leave in day_leave_intervals:
                holiday = leave.holiday_id
                current_leave_struct = leaves.setdefault(holiday.holiday_status_id, {
                    'name': holiday.holiday_status_id.name or _('Global Leaves'),
                    'sequence': 5,
                    'code': holiday.holiday_status_id.name or 'GLOBAL',
                    'number_of_days': 0.0,
                    'number_of_hours': 0.0,
                    'contract_id': contract.id,
                })
                current_leave_struct['number_of_hours'] += hours
                work_hours = calendar.get_work_hours_count(
                    tz.localize(datetime.combine(day, time.min)),
                    tz.localize(datetime.combine(day, time.max)),
                    compute_leaves=False,
                )
                if work_hours:
                    current_leave_struct['number_of_days'] += hours / work_hours

            # compute worked days
            work_data = contract.employee_id.get_work_days_data(day_from, day_to, calendar=contract.resource_calendar_id)
            attendances = {
                'name': _("Normal Working Days paid at 100%"),
                'sequence': 1,
                'code': 'WORK100',
                'number_of_days': work_data['days'],
                'number_of_hours': work_data['hours'],
                'contract_id': contract.id,
            }

            res.append(attendances)
            res.extend(leaves.values())
        return res


    @api.onchange('employee_id', 'date_from', 'date_to')
    def onchange_employee(self):

        print('\n---', 'onchange on payslip', '--onchange on payslip--\n')
        if (not self.employee_id) or (not self.date_from) or (not self.date_to):
            return

        employee = self.employee_id
        date_from = self.date_from
        date_to = self.date_to
        contract_ids = []

        ttyme = datetime.fromtimestamp(time_1.mktime(time_1.strptime(str(date_from), "%Y-%m-%d")))
        locale = self.env.context.get('lang') or 'en_US'
        self.name = _('Salary Slip of %s for %s') % (
            employee.name, tools.ustr(babel.dates.format_date(date=ttyme, format='MMMM-y', locale=locale)))
        self.company_id = employee.company_id

        print('\n---', self.env.context.get('contract'), '--dasdsadsada--\n')
        if not self.env.context.get('contract') or not self.contract_id:
            contract_ids = self.get_contract(employee, date_from, date_to)
            print('\n---', contract_ids, '--contract_ids--\n')
            if not contract_ids:
                return
            self.contract_id = self.env['hr.contract'].browse(contract_ids[0])

        if not self.contract_id.struct_id:
            return
        self.struct_id = self.contract_id.struct_id

        # computation of the salary input
        contracts = self.env['hr.contract'].browse(contract_ids)
        worked_days_line_ids = self.get_worked_day_lines(contracts, date_from, date_to)
        worked_days_lines = self.worked_days_line_ids.browse([])
        for r in worked_days_line_ids:
            worked_days_lines += worked_days_lines.new(r)
        self.worked_days_line_ids = worked_days_lines
        
        print('\n---', contracts, '--contracts--\n')
        if contracts:
            input_line_ids = self.get_inputs(contracts, date_from, date_to)
            input_lines = self.input_line_ids.browse([])
            for r in input_line_ids:
                input_lines += input_lines.new(r)
            self.input_line_ids = input_lines
        return


    # TODO move this function into hr_contract module, on hr.employee object
    @api.model
    def get_contract(self, employee, date_from, date_to):
        """
        @param employee: recordset of employee
        @param date_from: date field
        @param date_to: date field
        @return: returns the ids of all the contracts for the given employee that need to be considered for the given dates
        """
        # a contract is valid if it ends between the given dates
        clause_1 = ['&', ('date_end', '<=', date_to), ('date_end', '>=', date_from)]
        # OR if it starts between the given dates
        clause_2 = ['&', ('date_start', '<=', date_to), ('date_start', '>=', date_from)]
        # OR if it starts before the date_from and finish after the date_end (or never finish)
        clause_3 = ['&', ('date_start', '<=', date_from), '|', ('date_end', '=', False), ('date_end', '>=', date_to)]
        clause_final = [('employee_id', '=', employee.id), ('state', '=', 'open'), '|', '|'] + clause_1 + clause_2 + clause_3
        return self.env['hr.contract'].search(clause_final).ids


    def get_inputs(self, contract_ids, date_from, date_to):
        """This Compute the other inputs to employee payslip."""

        res = []

        structure_ids = contract_ids.get_all_structures()
        print('\n---', structure_ids, '--structure_ids--\n')
        rule_ids = self.env['hr.payroll.structure'].browse(structure_ids).get_all_rules()
        print('\n---', rule_ids, '--rule_ids--\n')
        sorted_rule_ids = [id for id, sequence in sorted(rule_ids, key=lambda x: x[1])]
        print('\n---', sorted_rule_ids, '--sorted_rule_ids--\n')
        inputs = self.env['hr.salary.rule'].browse(sorted_rule_ids).mapped('input_ids')
        print('\n---', contract_ids, inputs, '--contract_ids--\n')
        for contract in contract_ids:
            print('\n---', contract, '--contract--\n')
            for input in inputs:
                print('\n---', input, '--input--\n')
                input_data = {
                    'name': input.name,
                    'code': input.code,
                    'contract_id': contract.id,
                }
                res += [input_data]
        print(("In Super function"))
        print('\n---', res, '--res--\n')

        contract_obj = self.env['hr.contract']
        emp_id = contract_obj.browse(contract_ids[0].id).employee_id
        lon_obj = self.env['hr.loan'].search([('employee_id', '=', emp_id.id), ('state', '=', 'approve')])
        for loan in lon_obj:
            print('\n---', loan, '--loan--\n')
            for loan_line in loan.loan_lines:
                print('\n---', loan_line, 'From=', date_from, 'LDate=', loan_line.date,'To=', date_to, 'State=', loan_line.paid, '--loan_line--\n')
                if date_from <= loan_line.date <= date_to and not loan_line.paid:
                    for result in res:
                        print('\n---', result, '--result--\n')
                        if result.get('code') == 'LO':
                            result['amount'] = loan_line.amount
                            result['loan_line_id'] = loan_line.id
        return res

    def action_payslip_done(self):
        for line in self.input_line_ids:
            if line.loan_line_id:
                line.loan_line_id.paid = True
        return super(HrPayslip, self).action_payslip_done()


class ResourceMixin(models.AbstractModel):
    _inherit = "resource.mixin"

    def get_work_days_data(self, from_datetime, to_datetime, compute_leaves=True, calendar=None, domain=None):
        """
            By default the resource calendar is used, but it can be
            changed using the `calendar` argument.

            `domain` is used in order to recognise the leaves to take,
            None means default value ('time_type', '=', 'leave')

            Returns a dict {'days': n, 'hours': h} containing the
            quantity of working time expressed as days and as hours.
        """
        resource = self.resource_id
        calendar = calendar or self.resource_calendar_id

        # naive datetimes are made explicit in UTC
        if not from_datetime.tzinfo:
            from_datetime = from_datetime.replace(tzinfo=utc)
        if not to_datetime.tzinfo:
            to_datetime = to_datetime.replace(tzinfo=utc)

        # total hours per day: retrieve attendances with one extra day margin,
        # in order to compute the total hours on the first and last days
        from_full = from_datetime - timedelta(days=1)
        to_full = to_datetime + timedelta(days=1)
        intervals = calendar._attendance_intervals(from_full, to_full, resource)
        day_total = defaultdict(float)
        for start, stop, meta in intervals:
            day_total[start.date()] += (stop - start).total_seconds() / 3600

        # actual hours per day
        if compute_leaves:
            intervals = calendar._work_intervals(from_datetime, to_datetime, resource, domain)
        else:
            intervals = calendar._attendance_intervals(from_datetime, to_datetime, resource)
        day_hours = defaultdict(float)
        for start, stop, meta in intervals:
            day_hours[start.date()] += (stop - start).total_seconds() / 3600

        # compute number of days as quarters
        days = sum(
            float_utils.round(ROUNDING_FACTOR * day_hours[day] / day_total[day]) / ROUNDING_FACTOR
            for day in day_hours
        )
        return {
            'days': days,
            'hours': sum(day_hours.values()),
        }

    class HrPayrollStructure(models.Model):
        """
        Salary structure used to defined
        - Basic
        - Allowances
        - Deductions
        """
        _inherit = 'hr.payroll.structure'
        _description = 'Salary Structure'

        @api.model
        def _get_parent(self):
            return self.env.ref('hr_payroll_community.structure_base', False)

        # name = fields.Char(required=True)
        code = fields.Char(string='Reference', required=True)
        company_id = fields.Many2one('res.company', string='Company', required=True,
                                     copy=False, default=lambda self: self.env['res.company']._company_default_get())
        # note = fields.Text(string='Description')
        parent_id = fields.Many2one('hr.payroll.structure', string='Parent', default=_get_parent)
        children_ids = fields.One2many('hr.payroll.structure', 'parent_id', string='Children', copy=True)
        # rule_ids = fields.Many2many('hr.salary.rule', 'hr_structure_salary_rule_rel', 'struct_id', 'rule_id',
        #                             string='Salary Rules')

        # @api.constrains('parent_id')
        # def _check_parent_id(self):
        #     if not self._check_recursion():
        #         raise ValidationError(_('You cannot create a recursive salary structure.'))

        @api.returns('self', lambda value: value.id)
        def copy(self, default=None):
            self.ensure_one()
            default = dict(default or {}, code=_("%s (copy)") % (self.code))
            return super(HrPayrollStructure, self).copy(default)

        def get_all_rules(self):
            """
            @return: returns a list of tuple (id, sequence) of rules that are maybe to apply
            """
            all_rules = []
            for struct in self:
                all_rules += struct.rule_ids._recursive_search_of_rules()
            return all_rules

        def _get_parent_structure(self):
            parent = self.mapped('parent_id')
            if parent:
                parent = parent._get_parent_structure()
            return parent + self



class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'
    _order = 'sequence, id'
    _description = 'Salary Rule'

    parent_rule_id = fields.Many2one('hr.salary.rule', string='Parent Salary Rule', index=True)
    child_ids = fields.One2many('hr.salary.rule', 'parent_rule_id', string='Child Salary Rule', copy=True)
    input_ids = fields.One2many('hr.rule.input', 'input_id', string='Inputs', copy=True)

    @api.constrains('parent_rule_id')
    def _check_parent_rule_id(self):
        if not self._check_recursion(parent='parent_rule_id'):
            raise ValidationError(_('Error! You cannot create recursive hierarchy of Salary Rules.'))

    def _recursive_search_of_rules(self):
        """
        @return: returns a list of tuple (id, sequence) which are all the children of the passed rule_ids
        """
        children_rules = []
        for rule in self.filtered(lambda rule: rule.child_ids):
            children_rules += rule.child_ids._recursive_search_of_rules()
        return [(rule.id, rule.sequence) for rule in self] + children_rules



class HrRuleInput(models.Model):
    _name = 'hr.rule.input'
    _description = 'Salary Rule Input'

    name = fields.Char(string='Description', required=True)
    code = fields.Char(required=True, help="The code that can be used in the salary rules")
    input_id = fields.Many2one('hr.salary.rule', string='Salary Rule Input', required=True)