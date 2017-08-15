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

{
    'name': "Notification of products with accesories in stock pickings.",
    'description': """
        Extends addon stock for show a message in screen of stock picking at
        moment of validation that indicates that the picking contains products
        that has accesories.
    """,
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'category': 'Warehouse',
    'version': '0.1.0',
    'depends': ['stock'],
    'data': [
        'views/product_view.xml',
        'views/stock_view.xml',
    ],
    'demo': [
    ],
}
