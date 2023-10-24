import re
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'
    _inherit = ['person.mixin']

    name = fields.Char(string="Patient name")

    active = fields.Boolean(
        default=True, )
    date_of_birth = fields.Date(string='Patient date of birth', )
    age = fields.Integer(compute="_compute_age")
    passport_data = fields.Char(string='Patient Passport', )
    contact_person = fields.Char(string='Contact Person', )

    # doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', )
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        inverse_name='patient_id',
        string='Attending doctor'
    )
    personal_doctor_ids = fields.One2many(
        comodel_name='hr.hospital.personal.doctor.change',
        inverse_name='patient_id',
        string="Changed doctors"
    )

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                                   record.email)

            if valid_email is None:
                raise ValidationError(_('Please provide a valid E-mail'))

    # disease_ids = fields.Many2many(
    #     comodel_name='hr.hospital.disease', )
    # visits_ids = fields.Many2many(
    #     comodel_name='hr.hospital.visit', )

    # def write(self, vals):
    #     if 'attending_doctor_id' in vals:
    #         for rec in self:
    #             print(rec.id)
    #             rec.write({
    #                 'personal_doctor_ids': [(0, 0,
    #                                          {'date': fields.datetime.now(),
    #                                           'doctor_id': vals['attending_doctor_id'],
    #                                           'patient_id': rec.id})]})
    #             return super().write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self) -> None:
        for record in self:
            today = datetime.today().date()
            birthday = record.date_of_birth or today
            diff = ((today.month, today.day) < (birthday.month, birthday.day))
            record.age = today.year - birthday.year - diff

    @api.model
    def create(self, vals_list: dict) -> dict:
        result = super(Patient, self).create(vals_list)
        if result:
            self._history_change(result)
        return result

    def write(self, vals: dict) -> bool:
        result = super().write(vals)
        if result:
            self._history_change()
        return result

    @api.model
    def _history_change(self, val=None) -> None:
        patients = val or self
        for patient in patients:
            self.env["hr.hospital.personal.doctor.change"].create({
                'change_date': datetime.now(),
                'patient_id': patient.id,
                'doctor_id': patient.doctor_id.id,
            })

    def replace_patient_doctor(self) -> dict:

        patients_ids = []
        for record in self:
            patients_ids.append(record.id)
            return {"type": "ir.actions.act_window",
                     "name": _("Replace Doctor"),
                     "res_model": "hr.hospital.replace.doctor",
                     "target": "new",
                     "views": [[False, "form"]],
                     "view_mode": "form",
                     'context': {
                         'default_patient_ids': patients_ids,
                     }}
