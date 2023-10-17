

from odoo import models, fields, api, _, exceptions


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['person.mixin']

    name = fields.Char(string="Doctor name")
    specialty = fields.Char(string='Specialty of Doctor', )

    mentor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    intern_ids = fields.One2many(comodel_name='hr.hospital.doctor', inverse_name='mentor_id', string='Intern')

    @api.constrains('mentor_id')
    def _mentor_constrains(self):
        for record in self:
            if record.mentor_id._is_intern():
                raise exceptions.ValidationError(_('Intern ' + record.mentor_id.name + ' cannot be a mentor'))
            if record._is_mentor():
                raise exceptions.ValidationError(_('Mentor ' + record.name + ' cannot be a mentor'))

    def _is_intern(self):
        for record in self:
            return bool(record.mentor_id.id)

    def _is_mentor(self):
        for record in self:
            check_count = self.search_count([('mentor_id.id', '=', record.id)])
            return bool(check_count)
