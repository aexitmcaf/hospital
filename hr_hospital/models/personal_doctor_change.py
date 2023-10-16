from odoo import models, fields, api, _


class PersonalDoctorChange(models.Model):
    _name = 'hr.hospital.personal.doctor.change'
    _description = 'Hospital history personal doctor changes'

    name = fields.Char(string='History of personal doctor changes')
    date = fields.Datetime(readonly=True)

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient', readonly=True)
    attending_doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', readonly=True)


