# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#    Coded by: isaac (isaac@vauxoo.com)
############################################################################
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
##############################################################################

{
    "name" : "Migracion de Factura Electronica para Mexico (CFD) de 2.0 a 2.2",
    "version" : "1.0",
    "author" : "Vauxoo",
    "category" : "Localization/Mexico",
    "description" : """This module creates e-invoice files from invoices with standard CFD-2010 of Mexican SAT.
Requires the following programs:
  xsltproc
    Ubuntu insall with:
        sudo apt-get install xsltproc

  openssl
      Ubuntu insall with:
        sudo apt-get install openssl
    """,
    "website" : "www.vauxoo.com",
    "license" : "AGPL-3",
    "depends" : ["base","l10n_mx_facturae","l10n_mx_res_partner_bank_currency",
            "sale",#no depende de "sale" directamente, pero marca error en algunas versiones
        ],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        "pay_method_view.xml",
        "invoice_view.xml",
        "regimen_fiscal.xml",
        "partner_view.xml",
        "regimen_fiscal_data.xml",
#        "l10n_mx_facturae_report.xml",
 #       "l10n_mx_facturae_wizard6.xml",

#        "invoice_view.xml",

    ],
    "installable" : True,
    "active" : False,
}
