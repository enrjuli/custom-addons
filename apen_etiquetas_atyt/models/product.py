from odoo import fields, models, api


class ProductPackaging(models.Model):
    _inherit = 'product.packaging'
    
    product_active = fields.Boolean('Activo')
    
    

    
