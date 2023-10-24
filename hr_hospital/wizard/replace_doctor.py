from odoo import fields, models


class ReplaceDoctor(models.TransientModel):
    _name = 'hr.hospital.replace.doctor'
    _description = 'Replace the doctor'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_ids = fields.Many2many(comodel_name='hr.hospital.patient')

    def replace_doctor(self):
        self.ensure_one()
        doctor_id = self.doctor_id.id
        self.env["hr.hospital.patient"].search([('id', '=', self.id)]).write({
            'doctor_id': doctor_id
        })
