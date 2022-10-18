from odoo import models

class AccountMoveLine(models.Model):
    _inherit ="account.move.line"

    #CON ESTE METODO COMPARAMOS LA REFERENCIA INTERNA CON LA REFERENCIA DEL CLIENTE,
    #MEDIANTE EL MODULO EXTRA QUE ESTA EN DEPENDENCIAS
    def get_client_reference(self):
        name = self.name
        display_name = self.product_id.display_name

        id1 = name.index("[")
        id2 = name.index("]")

        id3 = display_name.index("[")
        id4 = display_name.index("]")

        ref_cliente = ""
        ref_intern = ""

        for i in  range(id1 + len("["), id2):
            ref_cliente = ref_cliente + name[i]
        
        for i in  range(id3 + len("["), id4):
            ref_intern = ref_intern + display_name[i]

        #SI LOS DOS CODIGOS SON IGUALES NO RETORNAMOS NADA, 
        #SI NO SE RETORNA LA REFERENCIA DEL CLIENTE PARA PODER MOSTRARLA EN EL INFORME
        if ref_cliente != ref_intern:
            return ref_cliente
        else:
            return ""
