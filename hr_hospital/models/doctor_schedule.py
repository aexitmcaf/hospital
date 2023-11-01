from odoo import models, fields, api, _, exceptions
from datetime import timedelta, datetime, time
from odoo.addons.hr_hospital import constants as const


class DoctorSchedule(models.Model):
    _name = 'hr.hospital.doctor.schedule'
    _description = 'Hospital doctor schedule'

    name = fields.Char(string='Hospital doctor schedule')
    # date_appointment = fields.Date(string='Date appointment')
    # time_appointment = fields.Datetime(string="Time appointment")
    # time_appointment = fields.Integer()
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        ondelete="cascade",
        required=True
    )

    visit_date = fields.Date(
        required=True,
        string="Work day"
    )

    day_week = fields.Char(
        string="Day of the week",
        compute="_compute_day_week"
    )

    shift_duration = fields.Selection(
        selection=const.SHIFT_DURATION,
        required=True,
        default="8"
    )

    start_time = fields.Datetime()
    shift_end_time = fields.Datetime(
        compute="_compute_shift_end_time",
        store=True
    )

    visit_ids = fields.One2many(
        comodel_name="hr.hospital.visit",
        inverse_name="schedule_id"
    )

    @api.onchange('visit_date', 'start_time')
    @api.depends('visit_date', 'start_time')
    def _compute_day_week(self):
        if self.visit_date:
            day_week = self.visit_date.strftime('%A')
            self.day_week = day_week.capitalize()
            if not self.start_time:
                start_time = datetime.combine(
                    self.visit_date, time(0,0,0)
                )
                self.start_time = start_time
            elif self.start_time:
                self.start_time = datetime.combine(
                    self.visit_date, self.start_time.time()
                )
        else:
            self.day_week = None

    def name_get(self) -> list:
        return [
            (schedule.id, f"[{schedule.visit_date}, "
                          f"{schedule.doctor_id.name}]") for schedule in self
        ]

    @api.onchange('visit_date', 'shift_duration')
    @api.depends('visit_date', 'shift_duration')
    def _compute_shift_end_time(self):
        for record in self:
            if record.start_time and record.shift_duration:
                shift_duration = int(record.shift_duration)
                shift_end_delta = timedelta(
                    hours=shift_duration, minutes=00, seconds=00
                )
                record.shift_end_time = record.start_time + shift_end_delta
            else:
                record.shift_end_time = None


    # @api.constrains('start_time', 'end_time')
    # def _check_date_validation(self):
    #     for record in self:
    #         if record.end_time < record.start_time:
    #             raise exceptions.ValidationError(_('End time should not be previous date.'))

    # @api.constrains('doctor_assigned_id', 'date_appointment', 'time_appointment')
    # def _check_date_validation(self):
    #     start_time = '09:00'
    #     end_time = '18:00'
    #     for record in self:
    #         t_date = datetime.strftime(record.create_date, "%H:%M")
    #         if t_date < start_time or t_date > end_time:
    #         # if record.time_appointment < start_time or record.time_appointment > end_time:
    #             raise exceptions.ValidationError(_('Appointment time should be between 09:00 - 18:00'))
    #         found_rec = self.search([('doctor_assigned_id.id', '=', record.doctor_assigned_id.id),
    #                                 ('time_appointment', '=', record.time_appointment),
    #                                 ('date_appointment', '=', record.date_appointment),
    #                                 ('id', '!=', record.id)])
    #         if found_rec:
    #             raise exceptions.ValidationError(_('Appointment already exist'))
