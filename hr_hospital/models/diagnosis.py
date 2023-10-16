from odoo import fields, models, api


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Hospital Doctor Diagnosis'

    name = fields.Char(string='Diagnosis', )
    date = fields.Datetime()
    doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor', )
    patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient', )
    appointment_of_treatment = fields.Char(string='Appointment of treatment', )
    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease', )

    state = fields.Selection(
        selection=[('draft', 'Draft'), ('done', 'Done')], default='draft',
        required=True, )

    comment = fields.Char(
        readonly=True, states={'draft': [('readonly', False)]}
    )

    def action_done(self):
        self.write({'state': 'done'})

    @api.model
    def cron_done(self):
        self.search([('date', '<', fields.Date.today())]).write(
            {'state': 'done'})

