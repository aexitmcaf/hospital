from odoo import models, fields


class Doctor(models.Model):

    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
