from odoo import fields, models


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Hospital Doctor Diagnosis'

    name = fields.Char(string='Diagnosis', )
    date = fields.Datetime()
    doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor', )
    patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient', )
    # disease_ids = fields.Many2many(
    #     comodel_name='hr.hospital.disease', )
    appointment_of_treatment = fields.Char(string='Appointment of treatment', )
    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease', )
