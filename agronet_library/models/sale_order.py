from datetime import date, timedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"
        
    def get_assigned_bo_line_partner(self):
        filters = [
            ("partner_id", "=", self.partner_id.id),
            ("remaining_qty", ">=", 1),
            ("currency_id", "=", self.currency_id.id),
            #("state", "=", "open"),
        ]        
        blankets =  self.env["sale.blanket.order.line"].search(filters)
        return {"domain": {"order_line.blanket_order_line": [("id", "in", blankets.id)]}}
    
    @api.onchange("partner_id")
    def onchange_partner_id(self):
        res = super().onchange_partner_id()
        if self.partner_id:
            return self.get_assigned_bo_line_partner()
        return res
    