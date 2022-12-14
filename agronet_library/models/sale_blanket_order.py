# -*- coding: utf-8 -*-

from odoo import _,models, fields, api
from odoo.tools.misc import format_date


class SaleBlanketOrder(models.Model):
    _inherit = 'sale.blanket.order'
    
    pendent_consumir = fields.Float(string="Pendent Consumir %",compute="_compute_pendent_consumir")
    
    
    @api.depends("line_ids.original_uom_qty",
                 "line_ids.delivered_uom_qty")
    def _compute_pendent_consumir(self):
        for blanket_order in self:
            original = 0
            entregada = 0
            if blanket_order.line_ids:
                for line in blanket_order.line_ids:
                    original += line.original_uom_qty
                    entregada += line.delivered_uom_qty
                blanket_order.pendent_consumir = 100 - ((entregada/original) * 100)
            else:
                blanket_order.pendent_consumir = 0        
        
class SaleBlanketOrderLine(models.Model):
    _inherit = 'sale.blanket.order.line'
    
    date_create = fields.Date(string="Data de entrada", default=fields.Datetime.now, readonly=True)
    
    qty_disponible = fields.Float(
        string="Cantidad Disponible",
        compute="_compute_quantities",
        digits=("Product Unit of Measure"),)
    
    @api.depends("original_uom_qty","delivered_uom_qty")
    def _compute_quantities(self):
        res = super()._compute_quantities()
        for line in self:
            line.qty_disponible = (line.original_uom_qty - line.delivered_uom_qty) 
        return res
    
    def name_get(self):
        result = []
        if self.env.context.get("from_sale_order"):
            for record in self:
                res = "[%s]" % record.order_id.product_id.display_name
                if record.date_schedule:
                    formatted_date = format_date(record.env, record.date_schedule)
                    res += " - {}: {}".format(_("Date Scheduled"), formatted_date)
                res += " ({}: {} {})".format(
                    _("remaining"),
                    record.remaining_uom_qty,
                    record.product_uom.name,
                )
                result.append((record.id, res))
            return result
        return super().name_get()