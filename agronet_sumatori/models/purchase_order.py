from odoo import api,fields,models

class PurchaseOrder(models.Model):
    _inherit='purchase.order'

    total_kilo = fields.Float(string='Kilograms totals',
        compute='_compute_kilograms', store=True, readonly=True)

    @api.depends('order_line')                                
    def _compute_kilograms(self):
        for order in self:
            kilos_total = 0
            for line in order.order_line:
                kilos_total += line.product_uom_qty
            order.total_kilo = kilos_total
