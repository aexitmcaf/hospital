from odoo import models, fields, api, _, exceptions
from datetime import timedelta, datetime


class DoctorSchedule(models.Model):
    _name = 'hr.hospital.doctor.schedule'
    _description = 'Hospital doctor schedule'

    name = fields.Char(string='Hospital doctor schedule')
    date_appointment = fields.Date(string='Date appointment')
    time_appointment = fields.Datetime(string="Time appointment")
    # time_appointment = fields.Integer()
    doctor_assigned_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    # @api.constrains('start_time', 'end_time')
    # def _check_date_validation(self):
    #     for record in self:
    #         if record.end_time < record.start_time:
    #             raise exceptions.ValidationError(_('End time should not be previous date.'))

    @api.constrains('doctor_assigned_id', 'date_appointment', 'time_appointment')
    def _check_date_validation(self):
        start_time = '09:00'
        end_time = '18:00'
        for record in self:
            t_date = datetime.strftime(record.create_date, "%H:%M")
            if t_date < start_time or t_date > end_time:
            # if record.time_appointment < start_time or record.time_appointment > end_time:
                raise exceptions.ValidationError(_('Appointment time should be between 09:00 - 18:00'))
            found_rec = self.search([('doctor_assigned_id.id', '=', record.doctor_assigned_id.id),
                                    ('time_appointment', '=', record.time_appointment),
                                    ('date_appointment', '=', record.date_appointment),
                                    ('id', '!=', record.id)])
            if found_rec:
                raise exceptions.ValidationError(_('Appointment already exist'))
