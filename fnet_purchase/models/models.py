from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = "Purchase Order"

    # name = fields.Char('Order Reference', required=True, index=True, copy=False, default='New')
    # date_order = fields.Datetime('Order Date', required=True)
    # company_id = fields.Many2one('res.company', 'Company', required=True, index=True)
    email_bool = fields.Boolean(string='Email with Customer name and address')
    expected_closing = fields.Date(string='Expected Closing')
    # company_id = fields.Many2one('res.partner', string='Company')


class PurchaseRequisition(models.Model):
    _inherit='purchase.requisition'
    _description = "Purchase Requisition"

    # customer_id = fields.Many2one('res.partner','Customer Name')
    oppor_id = fields.Many2one('crm.lead','Enquiry Reference', required=False)
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env['res.company']._company_default_get('purchase.requisition'))
    avg_margin_percentage = fields.Float(string='Average Margin Percentage')


class PurchaseOrderLines(models.Model):
    _inherit = 'purchase.order.line'
    _description = "PurchaseOrderLines"

    product_category_id = fields.Many2one('product.category', 'Product Category', change_default=True)
    company = fields.Many2one('res.company', 'Company')
    hsn_code = fields.Char('HSN Code')
    purchase_price = fields.Char('Purchase Price')
    schedule_date = fields.Datetime('Schedule Date')


class PurchaseRequisitionLines(models.Model):
    _inherit = "purchase.requisition.line"
    _description = "PurchaseRequisitionLines"

    # product_id = fields.Many2one('product.product', string='Product', domain=[('purchase_ok', '=', True)],
    #                              required=False)
    product_category_id=fields.Many2one('product.category','Product Category')
    description =fields.Text('Description')
    vendor =fields.Many2one('Vendor')


# class bid_received_line(models.Model):
#     _name = 'bid.received.line'

    # tender_id = fields.Many2one('purchase.requisition', 'Tender Reference')
    # valid_qoute = fields.Boolean('Select')
    # purchase_order_id = fields.Many2one('purchase.order', 'Purchase Quotes', readonly=True)
    # vender_id = fields.Many2one('res.partner', 'Supplier', readonly=True)
    # product_id = fields.Many2one('product.product', 'Product', readonly=True)
    # quantity = fields.Float('Quantity', readonly=True)
    # unit_measure = fields.Many2one('product.uom', 'Unit of Measure', readonly=True)
    # purchase_unit_price = fields.Float('Purchase Unit Price', readonly=True)
    # unit_price = fields.Float('Unit Price', readonly=True)
    # purchase_total_price = fields.Float('Purchase Price', readonly=True)
    # sub_total = fields.Float('Sub Total', readonly=True)


