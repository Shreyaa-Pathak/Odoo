{
    'name': 'Task Delete Notification',
    'version': '1.0',
    'depends': ['project', 'mail'],
    'author': 'Shreya Pathak',
    'category': 'Project',
    'description': 'Sends notifications when tasks are deleted',
    'data': [
        'data/task_delete_mail_template.xml',
    ],
    'installable': True,
    'application': False,
}
