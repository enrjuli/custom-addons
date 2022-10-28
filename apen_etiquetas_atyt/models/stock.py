from odoo import models

class StockPicking(models.Model):
    _inherit='stock.picking'
        
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

class StockProductionLot(models.Model):
    _inherit = ['stock.production.lot']
    
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
