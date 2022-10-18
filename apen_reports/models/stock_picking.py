from odoo import api, fields, models    

#--------ESTE METODO IMPRIME LOS NUMEROS DE SERIE EN UNA TABLA APARTE---------

class StockPicking(models.Model):
    _inherit="stock.picking"

    num_bultos = fields.Integer(string="Bultos", readonly=False)
    weight = fields.Float(readonly=False)
    
    def _get_stock_lot_values(self):
        """ Get and prepare data to show a table of invoiced lot on the invoice's report. """
        self.ensure_one()

        if self.state == 'draft':
            return False

        for line in self.move_line_ids_without_package:
            if line.lot_id.name != False:
                return True
        return False