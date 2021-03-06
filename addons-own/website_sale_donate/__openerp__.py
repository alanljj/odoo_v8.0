# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2010-2012 OpenERP s.a. (<http://openerp.com>).
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
    'name': "FRSTC Spendenshop",
    # Make sure this translation file is loaded last:
    # also you should start the server once with --i18n-overwrite to make sure latest translations are loaded from files
    'sequence': 550,
    'summary': """Shoperweiterungen für FRSTC""",
    'description': """

Anpassungen des Online-Shops für NPOs
=====================================

- Frei wählbarer Produktpreis
- Minimaler Betrag für freien Produktpreis kann festgelegt werden (wird in Form mit JS und bei POST-Data kontrolliert)
- Produktpreis kann in Produktübersichten ausgeblendet werden
- Produktmengenselektor kann ausgeblendet werden
- Zahlungsbox (Add to cart) kann für Produkte ausgeblendet werden
- Zahlungsintervall ist beim Produkt festlegbar
- Zahlungsintervalle können frei konfiguriert werden (Standardzahlungsintervalle werden automatisch vor-angelegt)
- Zahlungsintervall XMLID (externalid) Zahlungsintervall Name und arbitrary price werden in der so line gespeichert
- Direkter Checkout von Produkten ist einstellbar
- Forced Fields der Kontaktdaten können geändert werden!
- Standard Spendenprodukt wird angelegt (Donate)
- Standard Lieferart wird angelegt (None)
- VORBEREITET: Kontaktdaten werden auch mittels jquery validate überprüft! (Deaktiviert in templates.xml)
- Ausblenden der Steuer und Lieferkosten über Java Script wenn kleiner gleich 0 (nur in der cart page!)
- Lieferart ausblendbar per Checkbox
- Lieferadresse ausblendbar per Checkbox
- Wording für EN und DE im Shop wird auf NPOs ausgelegt! (Herausfinden und PS für Joe)
- x
- Ogone Bild austauschen für Website template :) Logo von Kreditkarten (payment_ogone_extended)
- sticky menu and other main menu stuff (website_main_menu)
- Öster Konten auto anlegen über base_config wenn ich das addon finde!

## Todo
- Checkout and Payment on a single Form - maybe also usable as snippet

    """,
    'author': "Datadialog - Michael Karrer",
    'website': "http://www.datadialog.net/",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'website_tools',
        'website_sale',
        'website_sale_delivery',
    ],
    'installable': True,
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
        'views/res_config.xml',
    ],
}
