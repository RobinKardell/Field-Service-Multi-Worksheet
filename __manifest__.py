{
    'name': 'Field Service Multi Worksheet',
    'version': '16.0.1.0.0',
    'category': 'Field Service',
    'summary': 'Add support for multiple worksheets in field service.',
    'author': 'Your Name or Company',
    'depends': ['fieldservice'],
    'data': [
        'views/worksheets_menu.xml',
        'views/worksheet_views.xml',
        'views/fieldservice_inherit_views.xml',
        'report/worksheet_report_templates.xml',
    ],
    'installable': True,
    'application': False,
}
