from odoo import models, fields, api, _, exceptions
from odoo.addons.hr_hospital import constants as const


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['person.mixin']
    _parent_name = "parent_id"

    name = fields.Char(string="Doctor name")
    specialty = fields.Char(string='Specialty of Doctor', )

    is_mentor = fields.Boolean()
    is_intern = fields.Boolean()
    active = fields.Boolean(default=True)

    # patient_ids = fields.One2many(
    #     comodel_name="hr.hospital.patient",
    #     inverse_name="doctor_id"
    # )

    state = fields.Selection(
        selection=const.DOCTOR_STATE_LIST,
        default="draft",
        string="Status"
    )

    parent_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        domain="[('is_mentor', '=', True)]",
        string="Mentor"
    )

    child_ids = fields.One2many(
        comodel_name="hr.hospital.doctor",
        inverse_name="parent_id",
        string="Interns"
    )

    schedule = fields.One2many(
        comodel_name="hr.hospital.doctor.schedule",
        inverse_name="doctor_id"
    )

    @api.model
    def create(self, vals_list):
        vals_list['state'] = "active"
        return super().create(vals_list)

    def write(self, vals):
        active = vals.get('active', "")
        for record in self:
            if active is False:
                record.state = 'arch'
        return super().write(vals)

    @api.onchange('is_intern')
    def onchange_is_intern(self):
        if not self.is_intern:
            self.parent_id = False

    @api.constrains('parent_id')
    def _check_mentor_recursion(self):
        if not self._check_recursion():
            raise exceptions.ValidationError(_('You cant create intern.'))

    # @api.constrains('mentor_id')
    # def _mentor_constrains(self):
    #     for record in self:
    #         if record.mentor_id._is_intern():
    #             raise exceptions.ValidationError(_('Intern ' + record.mentor_id.name + ' cannot be a mentor'))
    #         if record._is_mentor():
    #             raise exceptions.ValidationError(_('Mentor ' + record.name + ' cannot be a mentor'))
    #
    # def _is_intern(self):
    #     for record in self:
    #         return bool(record.mentor_id.id)
    #
    # def _is_mentor(self):
    #     for record in self:
    #         check_count = self.search_count([('mentor_id.id', '=', record.id)])
    #         return bool(check_count)
