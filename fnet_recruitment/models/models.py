
from odoo import models, fields, api

class Recruitment(models.Model):
    _name = 'recruitment.details'

    position_name = fields.Char(string="Position Name")
    department = fields.Char(string="Department Name")
    reason_vacancy = fields.Selection([('resignation', 'Resignation'),('termination','Termination'),('position','New Position')],string="Reason for the vacancy")
    whom_replacement = fields.Char(string="If Replacement then Replacement of whom")
    position_reason = fields.Char(string="If New Position, Reason for its creation")
    educational_qualification = fields.Char(string="Educational Qualification")
    area_of_exp = fields.Char(string=" Area of Expertise")
    other_skills = fields.Char(string=" Others Skills")
    salary = fields.Char(string="Salary in CTC")
    experiance = fields.Float(string="Year of Experience")
    filled_date = fields.Date(string="To be filled within the date")
    recruitment = fields.Selection([('naukri','Naukri'),('reference','Internal Reference'),('consultant','Consultant')],string="Recruitment Plan")
    description = fields.Text(string="Description")
    nda = fields.Binary(string="NDA")
    credit_days = fields.Integer(string="Credit Days")
    credit = fields.Integer(string="Credit Days")
    consultant_payment = fields.Selection([('cheque','Cheque'),('neft','NEFT')],string='Consultant mode of payment')
    cheque_no = fields.Char(string="Cheque no")
    date = fields.Date(string="Date")
    amount =fields.Char(string="Amount")
    utr_number = fields.Char(string="UTR number")
    social_media = fields.Char(string="Social Media")
    advertisement = fields.Char(string="Advertisement")
    job_fairs = fields.Selection([('sourced','No of CV Sourced'),('screening','Screening'),('initial_calls','Initial level Calls')],string="Job Fairs")

    initial_level_calls_ids = fields.One2many('call.details' ,'person_id',string="Initial level Calls")

    product_knowledge = fields.Char(string="Product Knowledge")
    technical_level = fields.Char(string="Technical Level")
    fitment = fields.Selection([('salary', 'Salary'), ('level', 'Level')], string="Fitment")
    technical_person = fields.Char(string="Status of Technical Person")

class Call(models.Model):
    _name = 'call.details'

    person_id = fields.Many2one('recruitment.details',string="Name")
    name_call = fields.Char(string="Name")
    contact_number = fields.Integer(string="Contact Number")
    position_ref = fields.Char(string="Position Referred for")
    current_ctc = fields.Char(string="Current CTC")
    expected_ctc = fields.Char(string="expected CTC")
    notice_period = fields.Selection([('negotiable','Negotiable'),('non_negotiable','Non Negotiable')],string="Notice Period")
    hr_status = fields.Char(string="HR Status")



