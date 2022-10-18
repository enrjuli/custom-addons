# -*- coding: utf-8 -*-
{
    'name': "apen_state_account",

    'summary': "Añade un estado al campo account",

    'description': """
        Long description of module's purpose
    """,

    'author': "Apen",
    'website': "http://www.apen.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'views/account_move_view.xml',
    ],
}
