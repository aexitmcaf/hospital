import re
from odoo import fields, models, api, exceptions, _


class PersonMixin(models.AbstractModel):
    _name = 'person.mixin'
    _description = 'Hospital Person Mixin'

    name = fields.Char(string='Person Name', required=True, tracking=True)
    address = fields.Char(string='Address')
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female')
    ], default="male", )
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email', required=True)
    image = fields.Binary(string='Image', )

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.email)

            if valid_email is None:
                raise exceptions.ValidationError(_('Please provide a valid E-mail'))