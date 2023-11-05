from odoo import fields, models, api


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Hospital Doctor Diagnosis'

    name = fields.Char(string='Diagnosis', )
    date = fields.Datetime()
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor', )
    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient', )
    appointment_of_treatment = fields.Text(string='Appointment of treatment', )
    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease', )
    diagnosis_date = fields.Date()
    comment = fields.Text()
    is_intern = fields.Boolean(compute="_compute_is_intern")
    treatment = fields.Text()

    def _compute_is_intern(self):
        for rec in self:
            rec.is_intern = rec.doctor_id.is_intern

    def name_get(self):
        return [
            (diagnosis.id, diagnosis.diagnosis_date) for diagnosis in self
        ]

    # state = fields.Selection(
    #     selection=[('draft', 'Draft'), ('done', 'Done')], default='draft',
    #     required=True, )
    # def action_done(self):
    #     self.write({'state': 'done'})
    #
    # @api.model
    # def cron_done(self):
    #     self.search([('date', '<', fields.Date.today())]).write(
    #         {'state': 'done'})
    #
