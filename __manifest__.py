# -*- coding: utf-8 -*-
{
    'name': 'Float field validation',
    'version': '17.1',
    'author': "PROGISTACK",
    'maintainer': "Abdoulaye K. Coulibaly",
    'category': 'Uncategorized',
    'sequence': 30,
    'summary': 'Float field validation',
    'description': """
    Float field validation
    """,
    'depends': ['base', 'stock'],
    'data': [
        'views/view.xml'
    ],

    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'float_field_validation/static/src/model/relational_model/record.js'
        ],
    }
}
