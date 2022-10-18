from odoo import models

#--------ESTE METODO HEREDA DEL PADRE PARA JUNTAR LOS PRODUCTOS, Y AÑADIMOS LOS CAMPOS QUE SOLO ESTAN EN LA VENTA--------

class StockMove(models.Model):
    _inherit="stock.move.line"

    def _get_aggregated_product_quantities(self, **kwargs):
        
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        
        entrada = False
        for lineas in self.sale_line:            
            num_serie = ""
            #MEDIANTE EL ATRIBUTO SALE_LINE OBTENEMOS LA LINEA DE VENTA CORRESPDIENTE CON TODOS LOS CAMPOS
            for aggregated_move_line in aggregated_move_lines:
                    
                if lineas.product_id.id == aggregated_move_lines[aggregated_move_line]['product'].id:
                    aggregated_move_lines[aggregated_move_line]['price_unit'] = lineas.price_unit
                    aggregated_move_lines[aggregated_move_line]['discount'] = lineas.discount
                    aggregated_move_lines[aggregated_move_line]['subtotal'] = lineas.price_subtotal  
                    aggregated_move_lines[aggregated_move_line]['lots'] = num_serie
                    
                    #CAMPS PER MOSTRAR REFERENCIES SOTA ELS PRODUCTES######################
                    #DE ESTA MANERA COMPARAMOS LA REFERENCIA INTERNA CON LA REFERENCIA DEL CLIENTE
                    ref_client = ""
                    ref_intern = ""

                    name = lineas.name
                    default_name = aggregated_move_line

                    if str.__contains__(name,"[") and str.__contains__(name,"]"):
                        id1 = name.index("[")
                        id2 = name.index("]")
                        
                        for i in  range(id1 + len("["), id2):
                            ref_client = ref_client + name[i]

                    if str.__contains__(name,"[") and str.__contains__(name,"]"):
                        id3 = default_name.index("[")
                        id4 = default_name.index("]")

                        for i in  range(id3 + len("["), id4):
                            ref_intern = ref_intern + default_name[i]
                 

                    aggregated_move_lines[aggregated_move_line]['ref_interna'] = lineas.product_id.default_code
                    aggregated_move_lines[aggregated_move_line]['origin_country'] = lineas.product_id.origin_country_id.name
                    if ref_client != ref_intern:
                        aggregated_move_lines[aggregated_move_line]['ref_client'] = ref_client
                    else:
                        aggregated_move_lines[aggregated_move_line]['ref_client'] = ""
                    ###########################################################################

                    aggregated_move_lines[aggregated_move_line]['estado'] = True
                    
                    entrada = True
                    a = 0
                    for lots in self.lot_id:
                        if lots.product_id.id == lineas.product_id.id:
                            if a > 0:
                                num_serie += ", "
                            num_serie += lots.name
                            aggregated_move_lines[aggregated_move_line]['lots'] = num_serie
                            a += 1
        if entrada == True:
            return aggregated_move_lines
        else:
            
            for aggregated_move_line in aggregated_move_lines:
                num_serie = ""
                a = 0
                aggregated_move_lines[aggregated_move_line]['ref_interna'] = ""
                aggregated_move_lines[aggregated_move_line]['origin_country'] = ""
                aggregated_move_lines[aggregated_move_line]['ref_client'] = ""
                
                for lots in self.lot_id:
                        if lots.product_id.id == aggregated_move_lines[aggregated_move_line]['product'].id:
                            if a > 0:
                                num_serie += ", "
                            num_serie += lots.name
                            aggregated_move_lines[aggregated_move_line]['lots'] = num_serie
                            a += 1

                aggregated_move_lines[aggregated_move_line]['estado'] = False
            return aggregated_move_lines
