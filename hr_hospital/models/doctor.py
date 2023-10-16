

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
        check_mentor = self.search([('mentor_id.id', '!=', False)])
        for rec in check_mentor:
            if rec == self.mentor_id:
                raise exceptions.ValidationError(_('Intern ' + rec.name + ' cannot be a mentor'))
