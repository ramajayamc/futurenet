
from odoo import models, fields, api


class Transfer(models.Model):
    _name = 'transfer.details'
    _description = "Transfer"

    type = fields.Selection([('internal','Internal'),('onsite','Onsite')], string="Type")
    transfer_ids = fields.One2many('transfer.employee','transfer_id', string='Transfer')
    state = fields.Selection([('new','New'),('submit','Submited'),('confirm','Confirm')],default='new')

    def object_submit(self):
        self.write({'state': 'submit'})

    def object_submit1(self):
        self.write({'state': 'confirm'})


class EmployeeTransfer(models.Model):
    _name = 'transfer.employee'
    _description = "EmployeeTransfer"

    transfer_id = fields.Many2one('transfer.details')
    type = fields.Selection([('internal','Internal'),('onsite','Onsite')], related='transfer_id.type', string="Type")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    current_job = fields.Many2one('hr.department',related='employee_id.department_id',string="Current Department")
    current_position = fields.Many2one('hr.job',related='employee_id.job_id',string="Current Position")
    to_job = fields.Many2one('hr.department',string="To Job")
    to_position = fields.Many2one('hr.job',string="To Position")
    current_location = fields.Many2one('res.partner',related='employee_id.address_id', string="Current Location")
    to_location = fields.Many2one('res.partner', string="To Location")

    # @api.model
    # def create(self, vals):
    #     result = super(EmployeeTransfer, self).create(vals)
    #     transfer = self.env['hr.employee']
    #     transfer.create({
    #         # 'address_id': self.to_location.id,
    #         'address_id': result.to_location.id,
    #
    #     })
    #     return result

    # def write(self, vals):
    #     if self.type == 'onsite':
    #         transfer_set = self.env['hr.employee'].search(
    #             [('employee_id', '=', self.id)])
    #         transfer = self.env['res.partner']
    #         if transfer_set:
    #             transfer.create({
    #                 'address_id': self.to_location.id,
    #             })
    #         else:
    #             transfer.create({
    #                 'address_id': self.to_location.id,
    #             })
    #
    #     if self.type:
    #         if self.type == 'onsite':
    #             transfer = self.env['transfer.employee'].search(
    #                 [('employee_id', '=', self.id)])
    #             transfer.update({
    #                 'address_id': self.to_location.id,
    #             })
    #     return super(EmployeeTransfer, self).write(vals)

