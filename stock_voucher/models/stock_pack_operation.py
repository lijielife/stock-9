# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, api


class StockPicking(models.Model):
    _inherit = 'stock.pack.operation'

    @api.multi
    @api.constrains(
        'product_qty',
        'qty_done',
    )
    def recompute_declared_value(self):
        """
        Recompute declared value. Used when qty changes not form view
        """
        self.mapped('picking_id').product_onchange()
