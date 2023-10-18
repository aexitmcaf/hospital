from odoo import models, fields, api, _


class PersonalDoctorChange(models.Model):
    _name = 'hr.hospital.personal.doctor.change'
    _description = 'Hospital history personal doctor changes'

    name = fields.Char(string='History of personal doctor changes')
    # change_date = fields.Datetime()

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Attending doctor')

    # def name_get(self) -> list:
    #     return [
    #         (change.change_date, change.patient_id.name) for change in self
    #     ]
