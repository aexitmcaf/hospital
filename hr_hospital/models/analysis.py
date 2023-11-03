from odoo import fields, models


class Analysis(models.Model):
    _name = 'hr.hospital.analysis'
    _description = 'Medical Analysis'

    name = fields.Char()
    price = fields.Float()
    active = fields.Boolean(default=True)


class AnalysisCard(models.Model):
    _name = 'hr.hospital.analysis.card'
    _description = 'Medical Analysis Card'

    analysis_id = fields.Many2one(
        comodel_name='hr.hospital.analysis',
        required=True
    )
    analysis_price = fields.Float(
        comodel_name='analysis_id.price',
        store=True
    )
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Doctor",
        required=True
    )
    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        required=True,
        ondelete='cascade'
    )

    analysis_date = fields.Datetime(default=fields.Datetime.now)
    result = fields.Text()
    active = fields.Boolean(default=True)



