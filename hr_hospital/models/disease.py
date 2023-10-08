from odoo import models, fields


class Disease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Hospital Patient Disease'

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
