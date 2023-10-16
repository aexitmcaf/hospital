from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Visit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Hospital Patient Visits'

    name = fields.Char(string='Patient Visits')
    date = fields.Datetime()
    visit_number = fields.Integer()
    start_time = fields.Datetime(string='Appointment time', default=fields.datetime.now())
    end_time = fields.Datetime(string='Appointment end', required=True,)

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor', )

    diagnosis_id = fields.Many2one(
        comodel_name='hr.hospital.diagnosis', )

    @api.constrains('start_time', 'end_time')
    def _check_date_validation(self):
        for record in self:
            if record.end_time < record.start_time:
                raise ValidationError(_('End time should not be previous date.'))
