import re

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class PersonMixin(models.AbstractModel):
    _name = 'person.mixin'
    _description = 'Hospital Person Mixin'

    name = fields.Char(string='Doctor Name', )
    address = fields.Char(string='Address')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default="male", )
    phone = fields.Char(string='Phone', )
    age = fields.Integer(string='Age', )
    email = fields.Char(string='Email', )
    image = fields.Binary(string='Image', )


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['person.mixin']

    specialty = fields.Char(string='Specialty of Doctor', )
    active = fields.Boolean(
        default=True, )

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.email)

            if valid_email is None:
                raise ValidationError(_('Please provide a valid E-mail'))
