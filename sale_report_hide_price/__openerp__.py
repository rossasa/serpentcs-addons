# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
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
    'name': 'Hide Price and Discount in Quotation Report',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'category': 'Sales Management',
    'website': 'http://www.serpentcs.com',
    'version': '8.0.1.0.1',
    'summary': 'Hide price/discount in Sale Order Report',
    'description': '''This module is to hide price/discount in Sale Order
Report.
It would give you 2 additional fields on Sales Order / Quotation:
1. Show Price
2. Show Discount
Based on the choices on the fields, the relevant fields would be shown on
the report.''',
    'depends': ['sale'],
    'data': [
        'views/sale_view.xml',
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'auto_install': False
}
