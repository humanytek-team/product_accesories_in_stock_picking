# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    products_has_accessories = fields.Boolean(
        'Has accesories ?',
        compute='_compute_products_has_accessories'
        )
    products_with_accessories = fields.Char(
        'Products with accessories',
        compute='_compute_products_with_accessories'
    )

    @api.depends('move_lines_related')
    def _compute_products_has_accessories(self):
        """Compute the value of field products_has_accessories"""

        for picking in self:
            picking.products_has_accessories = any(
                picking.mapped('move_lines_related.product_id.has_accessories')
                )

    @api.depends('products_has_accessories')
    def _compute_products_with_accessories(self):
        """Compute value of field products_with_accessories"""

        for picking in self:
            if picking.products_has_accessories:
                products_with_accessories = list()
                for move in picking.move_lines_related:
                    if move.product_id.has_accessories:
                        products_with_accessories.append(move.product_id.name)
                picking.products_with_accessories = ', '.join(
                    products_with_accessories)
            else:
                picking.products_with_accessories = False
