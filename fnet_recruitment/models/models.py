
from odoo import models, fields, api


class Recruitment(models.Model):
    _name = 'recruitment.details'
    _description = "Recruitment"

    position_name = fields.Char(string="Position Name")
    position_id = fields.Many2one('hr.applicant',string="Job Position")
    department = fields.Char(string="Department Name")
    reason_vacancy = fields.Selection([('resignation', 'Resignation'),('termination','Termination'),('position','New Position')], string="Reason for the vacancy")
    whom_replacement = fields.Char(string="If Replacement then Replacement of whom")
    position_reason = fields.Char(string="If New Position, Reason for its creation")
    educational_qualification = fields.Char(string="Educational Qualification")
    area_of_exp = fields.Char(string=" Area of Expertise")
    other_skills = fields.Char(string=" Others Skills")
    salary = fields.Char(string="Salary in CTC")
    experience = fields.Float(string="Year of Experience")
    filled_date = fields.Date(string="To be filled within the date")
    description = fields.Text(string="Description")
    state = fields.Selection([('new', 'New'),('submit', 'Submited'), ('done', 'Done'), ('cancel', 'Cancel')])

    def object_submit(self):
        self.write({'state': 'submit'})

    def object_done(self):
        self.write({'state': 'done'})

    def object_cancel(self):
        self.write({'state': 'cancel'})
        # self.write({'state': 'done'})

    def action_recruitment(self):
        # self.ensure_one()
        view_id = self.env.ref('hr_recruitment.hr_applicant_view_form').id
        return {
            "type": "ir.actions.act_window",
            "res_model": "hr.applicant",
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'view_id': view_id,
            # "views": [["form"]],
            'target': 'new',
            'context': {
                        'default_name': self.position_name,
                        'default_partner_id':self.id,
                        }
        }
        # return {
        #             'name': _('questionnaire'),
        #             'type': 'ir.actions.act_window',
        #             'view_type': 'form',
        #             'view_mode': 'form',
        #             'res_model': 'questionnaire.questionnaire',
        #             'views': [(view_id, 'form')],
        #             'view_id': view_id,
        #             'target': 'new',
        #             'context': {'default_name': self.name,
        #                         'default_partner_id':self.id,
        #                         }



class RecruitmentPlan(models.Model):
    _name = 'recruitment.plan'
    _description = "RecruitmentPlan"

    recruitment = fields.Selection([('job_portal','Job Portal'),('reference','Internal Reference'),('consultant','Consultant'),('social_media','Social Media'),('advertisement','Advertisement'),('job_fairs','Job Fairs'),('walkin','Walkins')], string="Recruitment Plan")
    nda = fields.Binary(string="NDA")
    credit_days = fields.Integer(string="Credit Days")
    # credit = fields.Integer(string="Credit Days")
    consultant_payment = fields.Selection([('cheque','Cheque'),('neft','NEFT')],string='Mode of payment')
    cheque_no = fields.Char(string="Cheque no")
    date = fields.Date(string="Date")
    amount =fields.Char(string="Amount")
    utr_number = fields.Char(string="UTR number")
    social_media = fields.Char(string="Social Media")
    advertisement = fields.Char(string="Advertisement")
    job_fair = fields.Selection([('initial_calls','Initial level Calls'),('technical','Technical Evaluation')],string="Job Fairs")

    initial_level_calls_ids = fields.One2many('call.details' ,'person_id',string="Initial level Calls")

    product_knowledge = fields.Char(string="Product Knowledge")
    technical_level = fields.Char(string="Technical Level")
    fitment_salary = fields.Char(string="Fitment Salary")
    fitment_level = fields.Char(string="Fitment Level")
    technical_person = fields.Char(string="Status of Technical Person")
    sourced = fields.Char(string="No of CV Sourced")
    screening = fields.Char(string="Screening")
    consultant_name = fields.Char(string="Consultant Name")
    hire = fields.Selection([('naukri','Naukri'),('indeed','Indeed'),('others','Others')], string="Hire Through")
    # type = fields.Selection([('naukri','Naukri'),('reference','Internal Reference'),('consultant','Consultant'),('social_media','Social Media'),('advertisement','Advertisement'),('job_fairs','Job Fair')], string="Recruitment Type")


class Call(models.Model):
    _name = 'call.details'
    _description = "Call"

    person_id = fields.Many2one('recruitment.plan' )
    name_call = fields.Char(string="Name")
    name_ref = fields.Char(string="Referred by")
    date = fields.Date(string="Interview Date")
    contact_number = fields.Integer(string="Contact Number")
    position_ref = fields.Char(string="Position Referred for")
    current_ctc = fields.Char(string="Current CTC")
    expected_ctc = fields.Char(string="expected CTC")
    notice_period = fields.Selection([('negotiable','Negotiable'),('non_negotiable','Non Negotiable')],string="Notice Period")
    hr_status = fields.Char(string="HR Status")
    remarks = fields.Char(string="Remarks")
    exp = fields.Char(string="Experience")
    ststus = fields.Selection([('select','Selected'),('reject','Rejected'),('hold','Hold')],string="Final Status")



class Applicant(models.Model):
    _inherit = 'hr.applicant'
    _description = "Applicant"

    recruitment_id = fields.Many2one('recruitment.details', string='Recruitment')


