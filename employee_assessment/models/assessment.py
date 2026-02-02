from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EmployeeAssessment(models.Model):
    _name = 'employee.assessment'
    _description = 'Employee Assessment'

    customer_id = fields.Char(string="Customer ID", required=True)
    name = fields.Char(string="Full Name", required=True)
    email = fields.Char(string="Email Address", required=True)
    department = fields.Char(string="Department", required=True)

    character = fields.Float(string="Character", required=True)
    punctuality = fields.Float(string="Punctuality", required=True)
    engagement = fields.Float(string="Employee Engagement", required=True)
    skills = fields.Float(string="Skills", required=True)

    final_score = fields.Float(string="Final Score", readonly=True)
    assessment_date = fields.Date(default=fields.Date.today)

    # Validation
    @api.constrains('character', 'punctuality', 'engagement', 'skills')
    def _check_scores(self):
        for rec in self:
            for field in [rec.character, rec.punctuality, rec.engagement, rec.skills]:
                if field < 0 or field > 100:
                    raise ValidationError("Scores must be between 0 and 100.")

    # Button Action
    def action_compute_score(self):
        for rec in self:
            if not all([rec.character, rec.punctuality, rec.engagement, rec.skills]):
                raise ValidationError("All assessment fields must be filled.")

            rec.final_score = (
                rec.character +
                rec.punctuality +
                rec.engagement +
                rec.skills
            ) / 4

            # Send Email
            template = self.env.ref('employee_assessment.email_template_assessment')
            template.send_mail(rec.id, force_send=True)
