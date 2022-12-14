{
    'name':'Etiquetas ZPL Personalizadas ',
    'summary': "Personalizacion de etiquetas para la impresion en ZPL ",
    'description': "Personalizacion de etiquetas para la impresion en ZPL", 
    'author': "Apen", 
    'website': "http://www.apen.es/", 
    'category': 'Reports', 
    'version': '14.0.1.0.1',
    "license": "AGPL-3", 
    'depends': ['base','stock','mrp','sale'],
    'data': [
        "reports/custom_report.xml",
        "reports/etiqueta_2_template_view.xml",
        "reports/etiqueta_1_template_view.xml", 
        "reports/etiqueta_3_production_template_view.xml",  
        "reports/etiqueta_trasferencias_view.xml",
        "reports/etiqueta_lote_template.xml",
        'views/mrp_production_form_inherit.xml',
        'views/product_packaging_inherit.xml'
    ], 
 }