from odoo import fields, models, api


class HrHospitalAddDiagnosisWizard(models.TransientModel):
    _name = 'hr.hospital.add.diagnosis'
    _description = 'Add Diagnosis'

    diagnosis_date = fields.Date()
    doctor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
    )
    patient_id = fields.Many2one(
        comodel_name="hr.hospital.patient",
        required=True
    )
    disease_id = fields.Many2one(
        comodel_name="hr.hospital.disease",
        string="Disease",
        index=True,
    )

    treatment = fields.Text(required=True)
    mentor_comment = fields.Text()
    is_intern = fields.Boolean()
    visit_id = fields.Integer()

    def add_diagnosis(self):
        for rec in self:
            result = self.env["hr.hospital.diagnosis"].create({
                'disease_id': rec.disease_id.id,
                'patient_id': rec.patient_id.id,
                'doctor_id': rec.doctor_id.id,
                'diagnosis_date': rec.diagnosis_date,
                'treatment': rec.treatment,
                'mentor_comment': rec.mentor_comment,
            })
            if result:
                vals = {
                    "diagnosis_id": result.id,
                    'is_done': True
                }
                visit = self.env[
                    "hr.hospital.visit"
                ].search([('id', '=', rec.visit_id)])
                visit.write(vals)

    @api.onchange('diagnosis_date')
    def _onchange_date(self):
        for rec in self:
            date_now = fields.Datetime.now().date()
            if rec.diagnosis_date:
                if rec.diagnosis_date < date_now:
                    rec.diagnosis_date = False