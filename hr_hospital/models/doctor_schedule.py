from odoo import models, fields, api, _, exceptions


class DoctorSchedule(models.Model):
    _name = 'hr.hospital.doctor.schedule'
    _description = 'Hospital doctor schedule'

    name = fields.Char(string='Hospital doctor schedule')
    start_time = fields.Datetime(string="Start appointment")
    end_time = fields.Datetime(string="End appointment")
    doctor_assigned_id = fields.Many2one(comodel_name='hr.hospital.doctor')

    @api.constrains('start_time', 'end_time')
    def _check_date_validation(self):
        for record in self:
            if record.end_time < record.start_time:
                raise exceptions.ValidationError(_('End time should not be previous date.'))