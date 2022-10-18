# -*- coding: utf-8 -*-

from odoo import _, fields, models, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    _description = 'Quants'

    metros_lineales = fields.Char(
        'Metros Lineales',
        help="Este calculo se calcula dividiendo la amplitud (Width) entre 1000 y el resultado entre la cantidad a mano en m2",
        compute='_compute_metros_lineales', size=10)
    
    @api.depends('product_id')
    def _compute_metros_lineales(self):
        for quant in self:
            id = quant.product_id.id
            if quant.product_id.uom_id.name.__eq__('m2') and id != False:
                width = self.search_values('Width',id)
                if width != "":
                    quant.metros_lineales = quant.inventory_quantity / (width/1000)
                else:
                    quant.metros_lineales = ""
            else:
                quant.metros_lineales = ""

    def search_values(self, attribute, id):
        
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
                    res = [int(i) for i in valor.split() if i.isdigit()]
                    if res.__len__() > 0:#COMPROVAMOS QUE EL WITDH SEA UN VALOR ENTERO, I SIN NINGUNA BARRA. ej(45 OK; 43/6 NO)
                        return res[0]
            
            return ""
           
                
