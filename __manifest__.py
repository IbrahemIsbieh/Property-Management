{
    'name': 'Property Management',
    'author': 'Ibrahem Issa',
    'version': '19.0.1.0.0',
    'category': 'Property',
    'summary' : 'Central management for properties, maintenance, sales and accounting',
    'depends': ['base', 'mail', 'account', 'app_onee','home_maintenance',
                'sale_management',],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/property_management_views.xml',
        'views/maintenance_management_views.xml',
        'views/dashboard_views.xml',
        'views/base_menu.xml',
        'views/integrate_menus.xml',


    ],
'assets': {
    'web.assets_backend': [
        'property_management/static/src/dashboard/dashboard.js',
        'property_management/static/src/dashboard/dashboard.xml',
        'property_management/static/src/dashboard/dashboard.css',
    ],
},


    'installable': True,
    'application': True,
}