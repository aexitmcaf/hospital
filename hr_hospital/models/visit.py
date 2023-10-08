from odoo import models, fields


class Visits(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Hospital Patient Visits'

    date = fields.Datetime()
    visit_number = fields.Integer()
