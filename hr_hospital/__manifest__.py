{
    'name': "Hospital",
    'summary': "Manage Hospital",

    'author': "Oleksandr",
    'website': "https://www.yourcompany.com",
    'category': "Customizations HR",
    'license': 'OPL-1',
    'version': '16.0.1.0.0',

    'depends': ['base'],
    # 'external_dependencies': {'python': [], },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visits_views.xml',
        'data/disease_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/patient_demo.xml',
        'demo/doctor_demo.xml',
    ],
}