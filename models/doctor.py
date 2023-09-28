import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
    isbn = fields.Char()
