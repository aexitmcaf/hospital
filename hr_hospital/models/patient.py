import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'
    _inherit = ['person.mixin']

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
    date_of_birth = fields.Date(string='Patient date of birth', )
    passport_data = fields.Char(string='Patient Passport', )
    contact_person = fields.Char(string='Contact Person', )
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor', )

    @api.constrains('age')
    def _check_patient_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError(_('Age must be greater than 0'))

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                                   record.email)

            if valid_email is None:
                raise ValidationError(_('Please provide a valid E-mail'))

    # disease_ids = fields.Many2many(
    #     comodel_name='hr.hospital.disease', )
    # visits_ids = fields.Many2many(
    #     comodel_name='hr.hospital.visit', )
