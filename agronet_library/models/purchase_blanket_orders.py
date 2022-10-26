# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseBlanketOrder(models.Model):
    _inherit = 'purchase.blanket.order.line'
    _description = "Purchase Blanket Order Lines"
    
    date_create = fields.Date(string="Data de entrada", default=fields.Datetime.now, readonly=True)
    
    qty_disponible = fields.Float(
        string="Cantidad Disponible",
        compute="_compute_quantities",
        digits=("Product Unit of Measure"),)
    
    @api.depends("original_uom_qty","received_uom_qty")
    def _compute_quantities(self):
        res = super()._compute_quantities()
        for line in self:
            line.qty_disponible = (line.original_uom_qty - line.received_uom_qty) 
        return res