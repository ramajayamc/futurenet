# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sales_targets(models.Model):
    _name = 'sale.target'
    _rec_name = 'name'
    _description = "sales_targets"

    name = fields.Char('Categ Name')
    category = fields.Selection([
        ('normal', 'Product'), ('cloud', 'Cloud EYE'), ('tech', 'Technical Support Group'), ('db', 'Database'),
        ('odoo', 'Odoo'), ('can', 'CAN'), ('tod', 'TOD'), ('rental', 'Rental'), ('tec', 'TEC'), ('top', 'TOP'),
        ('tor', 'TOR'), ('tos', 'TOS'),
        ('aws', 'AWS')], 'Category', default='normal',
        help="A category of the view type is a virtual category that can be used as the parent of another category to create a hierarchical structure.")
    team_ids = fields.Many2many('crm.team', 'team_target_rel', 'target_ids', 'team_id', 'Sales Team')
    from_date = fields.Date('Budget From Date')
    to_date = fields.Date('Budget To Date')

    total_funnel = fields.Float('Total Funnel')
    total_order_booked = fields.Float('Total Order Booked')
    total_tl_bill = fields.Float('Total TL Bill')
    total_bl_bill = fields.Float('Total BL Bill')

    target_line = fields.One2many('target.line', 'target_id', 'Target Line', copy=True)
    funnel_line = fields.One2many('funnel.line', 'funnel_id', 'Funnel Line', copy=True)
    order_booked_line = fields.One2many('booked.line', 'booked_id', 'Order Booked Line', copy=True)
    tl_billing_line = fields.One2many('tl.billing.line', 'tl_id', 'TL Billing Line', copy=True)
    bl_billing_line = fields.One2many('bl.billing.line', 'bl_id', 'BL Billing Line', copy=True)
    pay_receive_line = fields.One2many('pay.receive.line', 'prl_id', 'Payment Received Line', copy=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Confirm'),
    ], string='Status', readonly=True, copy=False, index=True, default='draft')

    # # ~ @api.one
    # # ~ @api.constrains('total_call')
    # # ~ def _check_no_call(self):
    # # ~ total_calls = 0.0
    # # ~ for st_calls in self.target_line:
    # # ~ total_calls = st_calls.call_count
    # # ~ if self.total_call < total_calls:
    # # ~ raise ValidationError(_("Sales Members Total Number Of Calls Should Be Less Than (Or) Equal To Total Calls"))
    #
    # # ~ @api.multi
    # @api.onchange('category')
    # def onchange_categeory_id(self):
    #     self.name = dict(self._fields['category'].selection).get(self.category)
    #
    # @api.multi
    # def def_confirm(self):
    #     self.write({'state': 'done'})


class target_lines(models.Model):
    _name = 'target.line'
    _description = "target_lines"

    target_id = fields.Many2one('sale.target', 'Target', ondelete='cascade')
    user_id = fields.Many2one('res.users', 'New Calls')
    call_count = fields.Char('Existing Calls')
    call_count1 = fields.Char('Follow Up')
    calls = fields.Char('Calls', default='Calls')

    @api.onchange('user_id')
    def _onchange_tem_salesperson(self):
        res = {}
        if self.env.context.get('team_ids'):
            crm_team_members_ids = self.env['res.users'].search(
                [('sale_team_id', 'in', self.env.context.get('team_ids')[0][2])])
            crm_sp_ids = crm_team_members_ids.ids
            userlist = list(set(crm_sp_ids))
            res['domain'] = {'user_id': [('id', 'in', userlist)]}
            return res
        else:
            res['domain'] = {'user_id': [('id', 'in', [])]}
            return res


class funnel_lines(models.Model):
    _name = 'funnel.line'
    _description = "funnel_lines"

    funnel_id = fields.Many2one('sale.target', 'Target', ondelete='cascade')
    user_id = fields.Many2one('res.users', 'Sales Person')
    funnel_count = fields.Float('Total')

    jan = fields.Float('Jan', default=0.0)
    feb = fields.Float('Feb', default=0.0)
    mar = fields.Float('March', default=0.0)
    apr = fields.Float('April', default=0.0)
    may = fields.Float('May', default=0.0)
    jun = fields.Float('June', default=0.0)
    jul = fields.Float('July', default=0.0)
    aug = fields.Float('Aug', default=0.0)
    sep = fields.Float('Sep', default=0.0)
    octt = fields.Float('Oct', default=0.0)
    nov = fields.Float('Nov', default=0.0)
    dec = fields.Float('Dec', default=0.0)
    funnel = fields.Char('Pipeline Per Week', default='Funnel')

    @api.onchange('user_id')
    def _onchange_tem_salesperson(self):
        res = {}
        if self.env.context.get('team_ids'):
            crm_team_members_ids = self.env['res.users'].search(
                [('sale_team_id', 'in', self.env.context.get('team_ids')[0][2])])
            crm_sp_ids = crm_team_members_ids.ids
            userlist = list(set(crm_sp_ids))
            res['domain'] = {'user_id': [('id', 'in', userlist)]}
            return res
        else:
            res['domain'] = {'user_id': [('id', 'in', [])]}
            return res

    @api.onchange('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octt', 'nov', 'dec')
    def _onchange_total_counts(self):
        totall_calls = 0.0
        self.funnel_count = self.jan + self.feb + self.mar + self.apr + self.may + self.jun + self.jul + self.aug + self.sep + self.octt + self.nov + self.dec


class booked_lines(models.Model):
    _name = 'booked.line'
    _description = "booked_lines"

    booked_id = fields.Many2one('sale.target', 'Target', ondelete='cascade')
    user_id = fields.Many2one('res.users', 'Sales Person')
    obl_count = fields.Float('Total')

    jan = fields.Float('Jan', default=0.0)
    feb = fields.Float('Feb', default=0.0)
    mar = fields.Float('March', default=0.0)
    apr = fields.Float('April', default=0.0)
    may = fields.Float('May', default=0.0)
    jun = fields.Float('June', default=0.0)
    jul = fields.Float('July', default=0.0)
    aug = fields.Float('Aug', default=0.0)
    sep = fields.Float('Sep', default=0.0)
    octt = fields.Float('Oct', default=0.0)
    nov = fields.Float('Nov', default=0.0)
    dec = fields.Float('Dec', default=0.0)
    order_booked = fields.Char('Order Booked', default='Order Booked')

    @api.onchange('user_id')
    def _onchange_tem_salesperson(self):
        res = {}
        if self.env.context.get('team_ids'):
            crm_team_members_ids = self.env['res.users'].search(
                [('sale_team_id', 'in', self.env.context.get('team_ids')[0][2])])
            crm_sp_ids = crm_team_members_ids.ids
            userlist = list(set(crm_sp_ids))
            res['domain'] = {'user_id': [('id', 'in', userlist)]}
            return res
        else:
            res['domain'] = {'user_id': [('id', 'in', [])]}
            return res

    @api.onchange('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octt', 'nov', 'dec')
    def _onchange_total_counts(self):
        totall_calls = 0.0
        self.obl_count = self.jan + self.feb + self.mar + self.apr + self.may + self.jun + self.jul + self.aug + self.sep + self.octt + self.nov + self.dec


class tl_billing_lines(models.Model):
    _name = 'tl.billing.line'
    _description = "tl_billing_lines"

    tl_id = fields.Many2one('sale.target', 'Target', ondelete='cascade')
    user_id = fields.Many2one('res.users', 'Sales Person')
    tl_count = fields.Float('Total')

    jan = fields.Float('Jan', default=0.0)
    feb = fields.Float('Feb', default=0.0)
    mar = fields.Float('March', default=0.0)
    apr = fields.Float('April', default=0.0)
    may = fields.Float('May', default=0.0)
    jun = fields.Float('June', default=0.0)
    jul = fields.Float('July', default=0.0)
    aug = fields.Float('Aug', default=0.0)
    sep = fields.Float('Sep', default=0.0)
    octt = fields.Float('Oct', default=0.0)
    nov = fields.Float('Nov', default=0.0)
    dec = fields.Float('Dec', default=0.0)
    tl_billing = fields.Char('TL Billing', default='TL Billing')

    @api.onchange('user_id')
    def _onchange_tem_salesperson(self):
        res = {}
        if self.env.context.get('team_ids'):
            crm_team_members_ids = self.env['res.users'].search(
                [('sale_team_id', 'in', self.env.context.get('team_ids')[0][2])])
            crm_sp_ids = crm_team_members_ids.ids
            userlist = list(set(crm_sp_ids))
            res['domain'] = {'user_id': [('id', 'in', userlist)]}
            return res
        else:
            res['domain'] = {'user_id': [('id', 'in', [])]}
            return res

    @api.onchange('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octt', 'nov', 'dec')
    def _onchange_total_counts(self):
        totall_calls = 0.0
        self.tl_count = self.jan + self.feb + self.mar + self.apr + self.may + self.jun + self.jul + self.aug + self.sep + self.octt + self.nov + self.dec


class bl_billing_lines(models.Model):
    _name = 'bl.billing.line'
    _description = "bl_billing_lines"

    bl_id = fields.Many2one('sale.target', 'Target', ondelete='cascade')
    user_id = fields.Many2one('res.users', 'Sales Person')
    bl_count = fields.Float('Total')

    jan = fields.Float('Jan', default=0.0)
    feb = fields.Float('Feb', default=0.0)
    mar = fields.Float('March', default=0.0)
    apr = fields.Float('April', default=0.0)
    may = fields.Float('May', default=0.0)
    jun = fields.Float('June', default=0.0)
    jul = fields.Float('July', default=0.0)
    aug = fields.Float('Aug', default=0.0)
    sep = fields.Float('Sep', default=0.0)
    octt = fields.Float('Oct', default=0.0)
    nov = fields.Float('Nov', default=0.0)
    dec = fields.Float('Dec', default=0.0)
    bl_billing = fields.Char('BL Billing', default='BL Billing')

    @api.onchange('user_id')
    def _onchange_tem_salesperson(self):
        res = {}
        if self.env.context.get('team_ids'):
            crm_team_members_ids = self.env['res.users'].search(
                [('sale_team_id', 'in', self.env.context.get('team_ids')[0][2])])
            crm_sp_ids = crm_team_members_ids.ids
            userlist = list(set(crm_sp_ids))
            res['domain'] = {'user_id': [('id', 'in', userlist)]}
            return res
        else:
            res['domain'] = {'user_id': [('id', 'in', [])]}
            return res

    @api.onchange('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octt', 'nov', 'dec')
    def _onchange_total_counts(self):
        totall_calls = 0.0
        self.bl_count = self.jan + self.feb + self.mar + self.apr + self.may + self.jun + self.jul + self.aug + self.sep + self.octt + self.nov + self.dec


class payment_received_lines(models.Model):
    _name = 'pay.receive.line'
    _description = "payment_received_lines"

    prl_id = fields.Many2one('sale.target', 'Target', ondelete='cascade')
    user_id = fields.Many2one('res.users', 'Sales Person')
    prl_count = fields.Float('Total')

    jan = fields.Float('Jan', default=0.0)
    feb = fields.Float('Feb', default=0.0)
    mar = fields.Float('March', default=0.0)
    apr = fields.Float('April', default=0.0)
    may = fields.Float('May', default=0.0)
    jun = fields.Float('June', default=0.0)
    jul = fields.Float('July', default=0.0)
    aug = fields.Float('Aug', default=0.0)
    sep = fields.Float('Sep', default=0.0)
    octt = fields.Float('Oct', default=0.0)
    nov = fields.Float('Nov', default=0.0)
    dec = fields.Float('Dec', default=0.0)
    pay_receive = fields.Char('Payment Received', default='Payment Received')

    @api.onchange('user_id')
    def _onchange_tem_salesperson(self):
        res = {}
        if self.env.context.get('team_ids'):
            crm_team_members_ids = self.env['res.users'].search(
                [('sale_team_id', 'in', self.env.context.get('team_ids')[0][2])])
            crm_sp_ids = crm_team_members_ids.ids
            userlist = list(set(crm_sp_ids))
            res['domain'] = {'user_id': [('id', 'in', userlist)]}
            return res
        else:
            res['domain'] = {'user_id': [('id', 'in', [])]}
            return res

    @api.onchange('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octt', 'nov', 'dec')
    def _onchange_total_counts(self):
        totall_calls = 0.0
        self.prl_count = self.jan + self.feb + self.mar + self.apr + self.may + self.jun + self.jul + self.aug + self.sep + self.octt + self.nov + self.dec
