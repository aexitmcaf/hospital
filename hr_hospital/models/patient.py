import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
    doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor', )
    disease_ids = fields.Many2many(
        comodel_name='hr.hospital.disease', )
    visits_ids = fields.Many2many(
        comodel_name='hr.hospital.visits', )
