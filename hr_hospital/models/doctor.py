

from odoo import models, fields


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['person.mixin']

    specialty = fields.Char(string='Specialty of Doctor', )
    active = fields.Boolean(
        default=True, )
