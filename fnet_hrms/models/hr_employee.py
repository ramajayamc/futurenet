
from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "HrEmployee"

    employee_no = fields.Char(string='Employee ID')
    fathers_name = fields.Char(string='Fathers Name')
    fathers_dob = fields.Date(string='Father Date Of Birth')
    mothers_name = fields.Char(string='Mothers Name')
    mothers_dob = fields.Date(string='Mothers Date Of Birth')
    # Marital_ststus = fields.Selection( [('single', 'Single '), ('married', 'Married')])
    spouse_name = fields.Char(string='Name Of The Spouse')
    dom = fields.Date(string='Name Of Married')
    spouse_dob = fields.Date(string='Spouse Date Of Birth')
    chile1 = fields.Char(string="Child Name")
    chile1_dob = fields.Date(string="Child Date Of Birth")
    chile2 = fields.Char(string="Child Name")
    chile2_dob = fields.Date(string="Child Date Of Birth")
    employee_type = fields.Selection([('trainee', 'Trainee '), ('permanent', 'Permanent'),('internship', 'Internship')], String="Employee Type")

    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    street_temp = fields.Char('Street')
    street_temp2 = fields.Char('Street2')
    zip_temp = fields.Char('Zip')
    city_temp = fields.Char('City')
    state_id_temp = fields.Many2one("res.country.state", string='State')
    country_id_temp = fields.Many2one('res.country', string='Country')

    course_ids = fields.One2many('course.details','employee_id',string='Course Details')

    name_of_company_ids = fields.One2many('work.details','employee_id',string='Work Details')

    name_aadhar = fields.Char(stirng="Name as per the document")
    doc_number = fields.Char(stirng="Document Number")
    upload = fields.Binary(stirng="Upload")
    name_pan = fields.Char(string="Name as per the document")
    doc_pan = fields.Char(string="Document Number")
    upload_pan = fields.Binary(string="Upload")
    name_passport = fields.Char(string="Name as per the document")
    doc_passport = fields.Integer(string="Document Number")
    issuing_authority_passport = fields.Char(string="Name of the issuing authority")
    plase_of_issue_passport = fields.Char(string="Place of issue")
    issued_date_passport = fields.Date(string="Issued date")
    expire_date_passport = fields.Date(string="Date of expire")
    name_bank = fields.Char(string="Name of the bank")
    acc_num_bank = fields.Integer(string="Account Number")
    ifsc = fields.Char(string="IFSC Code")
    branch = fields.Char(string="Branch Name")

    skills_ids = fields.One2many('skills.details', 'employee_id', string='Skills Details')

    doj_our_comapny = fields.Date(string="DOJ as Per Our Company")
    date_of_appoinment = fields.Date(string="Date of Appointment")
    app_letter_upload = fields.Binary(string="Appointment letter")
    date_of_confirmation = fields.Date(string="Date of confirmation")
    con_letter_upload = fields.Binary(string="Confirmation letter")
    epf_no = fields.Integer(string="EPF No")
    uan_no = fields.Integer(string="UAN No")
    dof_epf = fields.Integer(string="Date Of joining as per EPF")
    esic_no = fields.Integer(string="ESIC No")
    doj_esic = fields.Integer(string="Date Of joining as per ESIC")
    doj_gratuity = fields.Date(string="Date Of joining as per Gratuity")
    reliving_date = fields.Date(string="Reliving Date")
    reason_resignation = fields.Char(string="Reason for Resignation")
    Date_of_reliving = fields.Date(string="Date of Reliving")
    reliving_doc = fields.Binary(string="Reliving letter")
    exit_doc = fields.Binary(string="Exit Interview Form")
    clearance_doc = fields.Binary(string="No due clearance form")
    full_and_final_amunt = fields.Integer(string="Full and final settlement amount ")
    settlement_date = fields.Date(string="Settlement date")
    settlement = fields.Selection([('cheque','Cheque'),('neft','NEFT')], string="Settlement")
    fnf_letter = fields.Binary(string="FNF Letter")

    awards_ids = fields.One2many('awards.details', 'employee_id', string='Awards Received')

    asset_ids = fields.One2many('asset.details', 'employee_id', string='Asset Details')

    @api.model
    def create(self, vals):
        vals['employee_no'] = self.env['ir.sequence'].next_by_code('employee.sequence')
        result = super(HrEmployee, self).create(vals)
        return result


class CourseDetails(models.Model):
    _name = 'course.details'
    _description = "CourseDetails"

    employee_id = fields.Many2one('hr.employee', string='Course')
    name = fields.Selection([('x', 'X*'), ('xii', 'XII'),
                             ('diploma', 'Diploma'),('iti', 'ITI'),
                             ('ug', 'UG'),('pg', 'PG'),('doctorate', 'Doctorate'),
                             ('others', 'Others')],string="Course Name")
    institute = fields.Char(string="Name of the Institute")
    year = fields.Char(string="Year of pass out")
    mark = fields.Float(string="%Score")
    certificate = fields.Binary(string="Certificate")


class WorkDetails(models.Model):
    _name = 'work.details'
    _description = "WorkDetails"

    employee_id = fields.Many2one('hr.employee', string='Work Experience')
    company_name = fields.Char(string="Name of the company")
    year_of_exp = fields.Float(string="Total years of experience")
    nature_of_job = fields.Char(string="Nature of the job")
    reliving_reason = fields.Char(string="Reason for reliving")
    reliving = fields.Selection([('formal', 'Reliving is formal'),('informal','Reliving is Informal')], string="Reliving is formal/Informal")
    designation = fields.Char(string="Designation")
    appointment_letter = fields.Binary(string="Appointment Letter")
    reliving_letter = fields.Binary(string="Reliving Letter / Experience Certificate")
    pay_slip = fields.Binary(string="Last 3 month Pay slip / Bank Certificate")


class SkillsDetails(models.Model):
    _name = 'skills.details'
    _description = "SkillsDetails"

    employee_id = fields.Many2one('hr.employee', string='Skills Details')
    name_certificate = fields.Selection([('global', 'Global',), ('certification', 'Certification')],
                                        string="Name of the Certification")
    date_of_comp = fields.Date(string="Date of Completion")
    upload_skill = fields.Binary(string="Upload")


class AwardsReceived(models.Model):
    _name = 'awards.details'
    _description = "AwardsReceived"

    employee_id = fields.Many2one('hr.employee', string='Awards Received')
    category = fields.Char(string="Category")
    year = fields.Char(string="Year")


class AssetDetails(models.Model):
    _name = 'asset.details'
    _description = "AssetDetails"

    employee_id = fields.Many2one('hr.employee', string='Asset Details')
    equipment_type = fields.Char(string="Equipment Type")
    model = fields.Char(string="Model")
    serial_no = fields.Char(string="Serial Number")
    hand_over = fields.Char(string="Hand Over")
    description = fields.Char(string="Description")