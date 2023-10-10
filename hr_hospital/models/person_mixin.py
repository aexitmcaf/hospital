# from odoo import fields, models
#
#
#
# class PersonMixin(models.AbstractModel):
#     _name = 'person.mixin'
#     _description = 'Hospital Person Mixin'
#
#     name = fields.Char(string='Patient Name', required=True, tracking=True)
#     address = fields.Char(string='Address', tracking=True)
#     gender = fields.Selection([
#         ('male', 'Male'),
#         ('female', 'Female')
#     ], default="male", tracking=True)
#     phone = fields.Char(string='Phone', required=True, tracking=True)
#     age = fields.Integer(string='Age', required=True, tracking=True)
#     email = fields.Char(string='Email', tracking=True)
