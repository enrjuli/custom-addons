from odoo import fields, models


class ResPartner(models.Model):
    _inherit="res.partner"

    text_ventas = fields.Text(string="Text Ventas")
    text_albarans = fields.Text(string="Text Albarans")
    text_factures = fields.Text(string="Text Factures")
