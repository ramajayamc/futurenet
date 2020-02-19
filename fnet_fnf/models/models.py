
from odoo import models, fields, api


class FNF(models.Model):
    _name = 'fnf.details'
    _description = "FNF"

    employee_id = fields.Many2one("hr.employee",string="Employee Name")
    graduity_is = fields.Boolean(string="Gratuity")
    doj = fields.Date(string="Date Of Joining")
    dor = fields.Date(string="Date Of Resignation")
    basic = fields.Char(string="Last drawn basic")
    gratuity = fields.Char(string="Gratuity Calculation")
    doj_service = fields.Date(string="DOJ")
    doj_gratuity = fields.Date(string="Gratuity Date of joining")
    total = fields.Char(string="Total Amount to be paid")
    amount_lic_group = fields.Integer(string="Amount from LIC Group Police")
    amount_paid_futurenet = fields.Integer(string="Amount from to be paid from Futurenet")
    asset_details_ids = fields.One2many('asset.details', 'emp_id', string='Asset Details')


class AssetDetails(models.Model):
    _inherit = "asset.details"
    _description = "AssetDetails"

    emp_id = fields.Many2one('fnf.details', string='Asset Details')

