# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services Pvt. Ltd.
#                            (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'Product image for sale reports',
    'author': 'Serpent Consulting Services Pvt. Ltd.,\
             Odoo Community Association (OCA)',
    'category': 'Sales Management',
    'website': 'http://www.serpentcs.com',
    'version': '8.0.1.0.0',
    'sequence': 1,
    'depends': ['sale_layout', 'web_tree_image'],
    'data': [
        'views/sale_product_view.xml',
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'auto_install': False
}
