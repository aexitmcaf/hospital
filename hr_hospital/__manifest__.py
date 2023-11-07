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
        'data/disease_data.xml',
        'wizard/replace_doctor.xml',
        'wizard/create_appointment.xml',
        'wizard/add_diagnosis.xml',

        'views/menu_views.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/disease_views.xml',
        'views/visits_views.xml',
        'views/diagnosis_views.xml',
        'views/personal_doctor_change_views.xml',
        'views/doctor_schedule_views.xml',
        'views/analysis_views.xml',
        'views/analysis_card_views.xml',
        'reports/doctor_templates.xml',
        'reports/report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/patient_demo.xml',
        'demo/doctor_demo.xml',
    ],
}
