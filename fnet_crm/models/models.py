from odoo import models, fields, api
import datetime


class Lead(models.Model):
    _inherit = 'crm.lead'
    _description = "Lead"

    req = fields.Boolean(string="Product" )
    name1 = fields.Char(string="Opportunity ID",readonly=True, required=False)
    types = fields.Selection([('sale', 'Sale'), ('service', 'Service'), ('sal_ser', 'Sale and Service')], string = 'Type')
    product_id = fields.Many2one('product.product', string='Product')
    # oem = fields.Many2many('crm.oem', String='Product')
    oem = fields.Selection([('dell','Dell'),('hp','HP'),('hitachi','Hitachi'),('accer','Accer'),('asus','ASUS')], string = 'OEM')

    # @api.model
    # def create(self, vals):
    #
    #     result = super(FnetCrm, self).create(vals)
    #     Phonecall = self.env['voip.phonecall']
    #     Phonecall.create({
    #         'call_date': datetime.datetime.today(),
    #         'partner_id': result.partner_id.id,
    #         'name1': 'lead_meeting',
    #         'phonecall_type': 'incoming',
    #         'name': result.name,
    #         'phone': result.phone,
    #         'user_id': result.user_id.id,
    #         'state': 'open',
    #         # 'partner_mobile': res.mobile,
    #         'lead_id': result.id,
    #     })
    #     return result

    # @api.model
    # def create(self, vals):
    #     print("ssssssssssssssssssssssssssss", self)
    #     vals['name1'] = self.env['ir.sequence'].next_by_code('enquiry.sequence')
    #     rec = super(Lead, self).create(vals)
    #     return rec

    # @api.model
    # def create(self, vals):
    #
    #     return cid

    @api.model
    def create(self, vals):
        print('asdasdasdasdasdsadsadas', vals)
        vals['name1'] = self.env['ir.sequence'].next_by_code('enquiry.sequence')
        cid = super(Lead, self).create(vals)
        res = super(Lead, self).create(vals)
        Phonecall = self.env['voip.phonecall']
        Phonecall.create({
            'call_date': datetime.datetime.today(),
            'partner_id': res.partner_id.id,
            'name1': 'lead',
            'phonecall_type': 'incoming',
            'name': res.name,
            'phone': res.phone,
            'user_id': res.user_id.id,
            'state': 'open',
            # 'partner_mobile': res.mobile,
            'lead_id': res.id,
        })
        return res

    def action_new_quotation(self):
        print("ssssssssssssssssssssssssssssssss",self,)
        action = self.env.ref("sale_crm.sale_action_quotations_new").read()[0]
        action['context'] = {
            'search_default_opportunity_id': self.id,
            'default_opportunity_id': self.id,
            'search_default_partner_id': self.partner_id.id,
            'default_partner_id': self.partner_id.id,
            'default_team_id': self.team_id.id,
            'default_campaign_id': self.campaign_id.id,
            'default_medium_id': self.medium_id.id,
            'default_origin': self.name,
            'default_name': self.name,
            'default_source_id': self.source_id.id,
            'default_company_id': self.company_id.id or self.env.company.id,
            'default_types': self.types,
            'default_product_id': self.product_id.id,
            'default_oem': self.oem,
        }
        return action

    def write(self, vals):
        if self.type == 'opportunity':
            Phonecall_set = self.env['voip.phonecall'].search(
                [('opportunity_id', '=', self.id), ('name', '=', 'reply')])
            Phonecall = self.env['voip.phonecall']
            if Phonecall_set:
                Phonecall.create({
                    'call_date': datetime.datetime.today(),
                    'partner_id': self.partner_id.id,
                    'name1': 'opportunity',
                    'phonecall_type': 'incoming',
                    'name': self.name,
                    'phone': self.phone,
                    'user_id': self.user_id.id,
                    'state': 'open',
                    # 'partner_mobile': res.mobile,
                    'lead_id': self.id,
                })
            else:
                Phonecall.create({
                    'call_date': datetime.datetime.today(),
                    'partner_id': self.partner_id.id,
                    'name1': 'opportunity',
                    'phonecall_type': 'incoming',
                    'name': self.name,
                    'phone': self.phone,
                    'user_id': self.user_id.id,
                    'state': 'open',
                    # 'partner_mobile': res.mobile,
                    'lead_id': self.id,
                })

        if self.type:
            if self.type == 'opportunity':
                Phonecall = self.env['voip.phonecall'].search(
                    [('opportunity_id', '=', self.id), ('name', '=', 'opportunity')])
                Phonecall.update({
                    'call_date': datetime.datetime.today(),
                    'partner_id': self.partner_id.id,
                    'name1': 'opportunity',
                    'phonecall_type': 'incoming',
                    'name': self.name,
                    'phone': self.phone,
                    'user_id': self.user_id.id,
                    'state': 'open',
                    # 'partner_mobile': res.mobile,
                    'lead_id': self.id,
                })
        return super(Lead, self).write(vals)

class CalendarEvent(models.Model):
    """ Model for Calendar Event """
    _inherit = 'calendar.event'
    _description = "CalendarEvent"

    @api.model
    def create(self, vals):
        result = super(CalendarEvent, self).create(vals)
        Phonecall = self.env['voip.phonecall']
        Phonecall.create({
            'call_date': result.start_date,
            'partner_id': result.partner_id.id,
            'name1': 'lead_meeting',
            'phonecall_type': 'incoming',
            'name': result.name,
            'user_id': result.user_id.id,
            'state': 'open',
            # 'partner_mobile': res.mobile,
            # 'lead_id': vals.get('opportunity_id'),
        })
        return result


    # @api.model
    # def create(self, vals):
    #
    #     res = super(FnetCrm, self).create(vals)
    #     Phonecall = self.env['voip.phonecall']
    #     Phonecall.create({
    #         'call_date': datetime.datetime.today(),
    #         'partner_id': res.partner_id.id,
    #         'name1': 'lead',
    #         'phonecall_type': 'incoming',
    #         'name': res.name,
    #         'phone': res.phone,
    #         'user_id': res.user_id.id,
    #         'state': 'open',
    #         # 'partner_mobile': res.mobile,
    #         'lead_id': res.id,
    #     })
    #     return res


class CrmPhoneCalls(models.Model):
    _inherit = "voip.phonecall"
    _description = "CrmPhoneCalls"

    # call_sum = fields.Char('Call Summary', required=True)
    name1 = fields.Selection(
        [('database', 'Customer Research'), ('call', 'Customer Appointment fixing'), ('reply', 'Mail read/reply'),
         ('order', 'Order followup'), ('meeting', 'Vendor followup'), ('portal', 'Registration-Vendor/portal'),
         ('quotation', 'Proposal/Quotation'),
         ('followup', 'Other followup'), ('payment', 'Payment followup'),
         ('tender', 'Tender search/reading/preparation'), ('internalmeeting', 'Internal meeting'),
         ('report', 'Report/Review'),
         ('travel', 'Travel/Out of office'), ('customermeetingexisting', 'Customer meeting-Existing'),
         ('customermeetingnew', 'Customer meeting- New'),
         ('lead', 'Lead'), ('telecalling', 'Telecalling'),('lead_meeting', 'Lead Meeting'), ('opportunity', 'Opportunity'),
         ], string='Call Summary', required=True)
    lead_id = fields.Many2one('crm.lead', 'Lead')
    opportunity_id = fields.Many2one('crm.lead', 'Opportunity',
                                     ondelete='cascade', track_visibility='onchange')
    # partner_mobile = fields.Char('Mobile')