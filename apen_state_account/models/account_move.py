from odoo import fields, models


class AccountMove(models.Model):
    
    _inherit = 'account.move'

    state = fields.Selection(selection=[
            ('draft', 'Draft'),
            ('risk', 'On Risk'),
            ('posted', 'Posted'),
            ('cancel', 'Cancelled'),
        ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='draft')
    
    def button_risk(self):
        self.state = 'risk'

    def _compute_show_reset_to_draft_button(self):
          for move in self:
            move.show_reset_to_draft_button = not move.restrict_mode_hash_table and move.state in ('posted', 'cancel','risk')