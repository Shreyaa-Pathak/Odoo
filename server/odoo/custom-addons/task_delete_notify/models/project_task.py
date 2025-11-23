from odoo import models
import logging

_logger = logging.getLogger(__name__)

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def unlink(self):
        _logger.warning("==== TASK DELETE NOTIFICATION TRIGGERED ====")

        template = self.env.ref('task_delete_notify.task_delete_mail_template', raise_if_not_found=False)

        for task in self:
            if not template:
                _logger.warning("Template not found!")
                continue

            # Prepare recipients
            emails = [user.email for user in task.user_ids if user.email]
            pm = task.project_id.user_id
            if pm and pm.email:
                emails.append(pm.email)

            emails = list(set(emails))
            if not emails:
                _logger.warning("No email recipients found.")
                continue

            # Send email using template as mail.mail
            mail_id = template.send_mail(task.id, email_values={'email_to': ",".join(emails)}, force_send=True)
            _logger.warning(f"Email sent to: {emails}, mail_id={mail_id}")

        return super(ProjectTask, self).unlink()

