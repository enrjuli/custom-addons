from odoo import api,fields,models


class MrpProduction(models.Model):
    _inherit='mrp.production'

    cantidad_etiquetas = fields.Integer('Cantidad de etiquetas', readonly=False)
    cantidad_paquete = fields.Integer('Unidades por paquete', readonly=False)
    
    @api.onchange('product_id')
    def _get_package_qty(self):
        for order in self:
            if order.product_id.packaging_ids.qty:
                order.cantidad_paquete = order.product_id.packaging_ids.qty
            else:
                order.cantidad_paquete = 0
    
    def update_package_qty(self):
        if self.product_id.packaging_ids.qty:
            self.cantidad_paquete = self.product_id.packaging_ids.qty
        else:
            self.cantidad_paquete = 0
    
    def print_values(self, attribute, id):
                
        query = """SELECT combination_indices FROM product_product 
                                WHERE id = (%(id)s)"""

        self._cr.execute(query, {'id':id})
        combinations = self._cr.fetchall()
        combitations2 = combinations[0][0]
        atributes = combitations2.split(',')

        atribut = ""
        valor = ""
        if atributes[0] == '':
            return ""
        else:
            for ids in atributes:
                
                query = """SELECT e.name, p.name FROM product_template_attribute_value a 
                                    LEFT JOIN product_attribute_value p 
                                    ON a.product_attribute_value_id = p.id
                                    LEFT JOIN product_attribute e
                                    ON a.attribute_id = e.id
                                    WHERE a.id = (%(id)s)"""
                        
                self._cr.execute(query, {'id':ids})
                data = self._cr.fetchall()
                atribut = data[0][0]
                valor =  data[0][1]
                
                if atribut == attribute:
                    return valor
            return ""
           