from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit='sale.order'

    total_kilo = fields.Float(string='Kilograms totals',
        compute='_compute_kilos', store=True, readonly=True)
    
    @api.depends('order_line')
    def _compute_kilos(self):
        for order in self:
            total_kilo = 0
            for lines in order.order_line:
                total_kilo += lines.product_uom_qty
            order.total_kilo = total_kilo
        