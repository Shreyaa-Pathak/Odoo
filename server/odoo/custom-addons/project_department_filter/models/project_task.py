from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = "project.task"

    # Department derived from project
    department_id = fields.Many2one(
        "hr.department",
        related="project_id.x_department_id",
        store=False
    )
