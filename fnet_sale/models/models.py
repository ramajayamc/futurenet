
from odoo import models, fields, api, _
from odoo.exceptions import UserError,except_orm



class SaleOrder(models.Model):
    _inherit = 'sale.order'


    types = fields.Selection([('sale', 'Sale'), ('service', 'Service'), ('sal_ser', 'Sale and Service')], String = 'Type')
    product_id = fields.Many2one('product.product', String='Product')
    oem = fields.Selection([('dell' ,'Dell') ,('hp' ,'HP') ,('hitachi' ,'Hitachi') ,('accer' ,'Accer') ,('asus' ,'ASUS')], String = 'OEM')
    quotation_reference = fields.Char("Quotation reference", readonly=True)
    tender_id = fields.Many2one('purchase.requisition', 'Tender Reference')
    enquiry_id = fields.Many2one('crm.lead', 'Enquiry Reference')
    confirmation_date = fields.Datetime(string='Confirmation Date', index=True, help="Date on which the sale order is confirmed.", oldname="date_confirm")
    # description = fields.Boolean(string="Two line description")
    pdf = fields.Boolean(string="A4 Sheet PDF Print", default=True)
    # set_notes = fields.Boolean(string="Set To True If Quotation Contains Notes", default=False)
    # product_line_ids = fields.Many2many('Margin Details')
    product_line_id = fields.One2many('product.order.line','order_id', string='Margin Details')

    # product_line_ids = fields.Many2many("product.move", string='Invoices', compute="_get_invoiced", readonly=True, copy=False)







    def action_confirm(self):
        ret_val = self.env['ir.attachment'].search(['|', ('res_id', '=', self.id), ('res_name', '=', self.name)])
        if ret_val:
            self.quotation_reference = self.name
            val = self.env['ir.sequence'].next_by_code('confirm.sale')
            self.write({'name': val})
            return super(SaleOrder, self).action_confirm()
        else:
            raise UserError(_('Please add the files in attachment.'))


class SaleOrderline(models.Model):
    _inherit = 'sale.order.line'

    hsn_code = fields.Char('HSN code')



class MarginDetails(models.Model):
    _name = 'product.order.line'


    order_id = fields.Many2one('Product')
    sale_value = fields.Char('Sale Price')
    purchase_value = fields.Char('Purchase Price')
    maregin_value = fields.Char('Margin')