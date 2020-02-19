# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class QuestionnaireRecord(models.Model):
    _name = "questionnaire.questionnaire"
    _description = "QuestionnaireRecord"

    headquarters = fields.Char(string='Headquarters')
    location = fields.Char(string='No Of Location')
    name = fields.Char(string="Name",readonly=True)
    partner_id = fields.Many2one('res.partner',string='Partner')

    no_of_users = fields.Selection([('user', '0-100'), ('users', '101-500'), ('above', 'Above 500')], string='No Of Users')
    specify_no_of_users = fields.Char(string='No Of Users Specify')
    server_storage = fields.Selection([('dell', 'Dell'), ('hp', 'HP'), ('ibm', 'IBM'),('others','Others'),('none','None')], string='Server/Storage')
    specify1_server_storage = fields.Char(string='Server/Storage Specify')
    server_hosted = fields.Selection([('on', 'On Premises'), ('cloud', 'Cloud'),('others','Others')], string='Server Hosted')
    specify2_server_hosted = fields.Char(string='Server Hosted Specify')
    is_server_vir = fields.Selection([('yes','YES'),('no','NO'),('none','None')], string='Server Virtualized')
    server_vir = fields.Selection([('vm', 'VMware'), ('re', 'Redhat'),('others','Others')], string='Server Type')
    specify3_server_vir = fields.Char(string='Server Type Specify')
    version = fields.Char(string='Version')
    osu = fields.Selection([('wind', 'Windows'), ('unix', 'Unix'),('others','Others')], string='Operating System Used')
    specify4_osu = fields.Char(string='Operating System Used Specify')
    database = fields.Selection([('oracle', 'Oracle'), ('mysql', 'MySQL'),('others','Others')], string='Database')
    specify6_database = fields.Char(string='Database Specify')
    message_colla = fields.Selection([('exchange', 'Exchange'), ('office', 'Office 365'),('google','Google Apps'),('open','Open Source'),('others','Others')], string='Messaging/Collaboration')
    specify7_message_colla = fields.Char(string='Messaging/Collaboration Specify')
    ticketing_tool = fields.Selection([('manage', 'Manage Engine'), ('otrs', 'OTRS'),('bmc',' BMC Remedy'),('others','Others'),('none','None')], string='Ticketing Tool/Complaints Manager')
    specify8_ticketing_tool = fields.Char(string='Ticketing Tool/Complaints Manager Specify')
    backup = fields.Selection([('rec', 'Recova'), ('mini', 'Minitool Data Recovery'),('others','Others'),('none','None')], string='Backup/Recovery')
    specify9_backup = fields.Char(string='Backup/Recovery Specify')


    application = fields.Selection([('erp', 'ERP'), ('crm', 'CRM'),('contant','Content/Document Management Tool'),('none','None')], string='Application Used')
    specify0_application = fields.Char(string='Application Used Specify')
    business = fields.Selection([('cog', 'Cognos'), ('pen', 'Pentaho'),('business','Business Object'),('others','Others '),('none','None')], string='Business Intelligence Tool')
    specify11_business = fields.Char(string='Business Intelligence Tool Specify')
    reporting_tool = fields.Selection([('share', 'Sharepoint'), ('qli', 'Qlikview'),('others','Others '),('none','None')], string='Reporting Tool')
    specify22_reporting_tool = fields.Char(string='Reporting Tool Specify')


    it_sup = fields.Selection([('manag', 'Managed Service'), ('in', 'In House'),('none','None')], string='IT Support(L1/L2)')
    specify33_it_sup = fields.Char(string='IT Support(L1/L2) Specify')
    security = fields.Selection([('cyber', 'Cyberoam'), ('dell', 'Dell Sonic Wall'),('others', 'Others'),('none','None')], string='Security and gateway')
    specify44_security = fields.Char(string='Security and gateway Specify')


class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = "ResPartner"

    # ~ headquarters = fields.Char(string='Headquarters')
    # ~ location = fields.Char(string='No Of Location')
    def questionnaire1_form(self):
        """ Return an action to open the document ``self``. This method is meant
            to be overridden in addons that want to give specific view ids for
            example.
        """
        rec = self.env['questionnaire.questionnaire'].search([('partner_id', '=', self.id)], limit=1)
        if rec:
            view_id = self.env.ref('fnet_q.view_questionnaire_form_view').id
            return {
                'name': _('questionnaire'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'questionnaire.questionnaire',
                'views': [(view_id, 'form')],
                'view_id': view_id,
                'target': 'current',
                'res_id': rec.id,
            }

        else:
            view_id = self.env.ref('fnet_q.view_questionnaire_form_view').id
            return {
                'name': _('questionnaire'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'questionnaire.questionnaire',
                'views': [(view_id, 'form')],
                'view_id': view_id,
                'target': 'new',
                'context': {'default_name': self.name,
                            'default_partner_id':self.id,
                            }
            }

