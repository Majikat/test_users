# -*- coding: utf-8 -*-

{
    'name': "Test Users",

    'summary': """
Fills the database with dummy users with specific rights, so it does
not get more painful to get enough users for right tests.
    """,

    'description': """
Bootstrap your testing sessions with out-of-the-box users ready to
serve.
    """,

    'author': "Majikat",
    'website': "http://majikat.com",

    'category': 'Extra Rights',
    'version': '1.0.0',

    'depends': ['base', 'sale', 'account', 'purchase', 'hr', 'stock',
                'manifest_translator'],

    'data': [
        'data/users.xml'
    ],
    'installable': True,
    'auto_install': False
}
