{
    'name': 'Employee Assessment',
    'version': '1.0',
    'summary': 'Assess employees/customers and send results via email',
    'author': 'Einstein',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/assessment_views.xml',
        'data/email_template.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}
