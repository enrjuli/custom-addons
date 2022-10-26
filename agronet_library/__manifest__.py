# -*- coding: utf-8 -*-
{
    'name': "agronet_library",

    'summary': """Modificacions varias per les blanket orders""",

    'description': """
        Modificacions varias per les blanket orders
    """,

    'author': "Apen",
    'website': "http://www.apen.es",
    'category': 'Compras y Ventas',
    'version': '14.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale','purchase_blanket_order','sale_blanket_order'],

    # always loaded
    'data': [
        'views/purchase_blanket_order_views.xml',
        'views/sale_blanket_order_views.xml',
    ],
}
