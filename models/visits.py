import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Visits(models.Model):
    _name = 'hr.hospital.visits'
    _description = 'Visits'

    name = fields.Char()
    visits = fields.Char()
