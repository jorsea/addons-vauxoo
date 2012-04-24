#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Vauxoo C.A.           
#    Planified by: Nhomar Hernandez
#    Audited by: Vauxoo C.A.
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

from osv import fields, osv
import tools
from tools.translate import _
from tools import config
import netsvc
import decimal_precision as dp

#~ class decorador_ll(osv.osv):
    #~ _name = 'decorador.decorador'
    #~ _columns = {}
    #~ 
    #~ def __init__(self, name, value, exc_type='warning'):
        #~ self.name = name
        #~ self.exc_type = exc_type
        #~ self.value = value
        #~ self.args = (exc_type, name)
        #~ 
    #~ def __call__(self, *args):
        #~ print self,args
        #~ newargs=self.mapping(args, self.f)
        #~ print "args",args
        #~ self.f (newargs[0],2,1,3,5)
        #~ 
    #~ def mapping(self, algo, orm):
        #~ print orm.__name__
        #~ if "write":
            #~ "logicamapeado"
        #~ if "create":
            #~ "logica de mapeado"
        #~ return algo
#~ decorador_ll()


class cost_structure(osv.osv):
    
    
    _name = 'cost.structure'
    _columns = {
    'description':fields.char('Description',size=128,help="Product Description"),
    'type':fields.selection([('v', 'Venta'),('C', 'Compra')], 'Type', help="Product type"),
    'serial':fields.boolean('Serial',help="Product Serial"),
    'date_reg':fields.datetime('Registr Date',help="Date to registre"),
    'cost_ult':fields.float('Ult Cost',digits_compute=dp.get_precision('Cost Structure'), help="Last Cost"),
    'qty_ult':fields.float('Last Qty',digits_compute=dp.get_precision('Cost Structure'), help="Last Qty"),
    'cost_prom':fields.float('Prom Cost',digits_compute=dp.get_precision('Cost Structure'),help="Avarage Cost"),
    'cost_suppler':fields.float('Supplier Cost',digits_compute=dp.get_precision('Cost Structure'),help="Supplier Cost"),
    'cost_ant':fields.float('Ant Cost',digits_compute=dp.get_precision('Cost Structure'),help="Ant Cost"),
    'qty_ant':fields.float('Ant Qty',digits_compute=dp.get_precision('Cost Structure'),help="Last Qty"),
    'ult_om':fields.many2one('product.uom','Ult UOM',),
    'prom_om':fields.many2one('product.uom','Prom UOM',),
    'ant_om':fields.many2one('product.uom','Ant UOM',),
    'date_cost_ult':fields.datetime('Date',help="Date of last change to last cost"),
    'date_ult_om':fields.datetime('Date',help="Date of last change to last UOM"),
    'date_cost_prom':fields.datetime('Date',help="Date of last change to avarage cost"),
    'date_prom_om':fields.datetime('Date',help="Date of last change to avarage UOM"),
    'date_cost_suppler':fields.datetime('Date',help="Date of last change to Supplier cost"),
    'date_ant_om':fields.datetime('Date',help="Date of last change to ant UOM"),
    'date_cost_ant':fields.datetime('Date',help="Date of last change to ant cost"),
    'date_cost_to_price':fields.datetime('Date',help="Date of last change to selection cost"),
    'min_margin':fields.float('% Margin',digits_compute=dp.get_precision('Cost Structure'),help="Porcent Margin Min"),
    'amount':fields.float('Amount',digits_compute=dp.get_precision('Cost Structure'),help="Amount"),
    'cost_to_price':fields.selection([('cost_ult', 'Ultimo Costo'),('cost_prom', 'Costo Promedio'),('cost_suppler', 'Costo Proveedor'),('cost_ant', 'Costo Anterior')], 'Type Cost', help="Product type"),
    'method_cost_ids':fields.one2many('method.price','cost_structure_id','Cost Method'),
    'company_id':fields.many2one('res.company','Company'),
    
    }
    _rec_name = 'description'
    
    _defaults = {
    'company_id':lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid,'cost.structure', context=c),
    
    
    
    }
    
    
cost_structure()

class method_price(osv.osv):
    
    def name_get(self,cr, uid, ids, context):
        if not len(ids):
            return []
        reads = self.browse(cr, uid, ids, context)
        res = []
        for r in reads:
            name = 'Price %d %s' % (r.sequence,repr(round(r.unit_price,3)))
            res.append((r.id, name))
        return res

    _name = 'method.price'
    _columns = {
    'cost_structure_id':fields.many2one('cost.structure','Cost Structure'),
    'sequence':fields.integer('Sequence'),
    'unit_price':fields.float('Price Unit',digits_compute=dp.get_precision('Cost Structure'),help="Price Unit"),
    'date':fields.date('Date'),
    'date_prom_begin':fields.date('Date Prom',help="Compute Date Prom"),
    'date_prom_end':fields.date('Date End',help="Compute Date Prom with end"),
    'margin':fields.float('Margin',digits_compute=dp.get_precision('Cost Structure'),help="Price Margin"),
    'arancel':fields.float('% Arancel',digits_compute=dp.get_precision('Cost Structure'),help="Porcent Arancel"),
    'min_margin':fields.float('% Margin',digits_compute=dp.get_precision('Cost Structure'),help="Porcent Margin Min"),
    'price_referen':fields.float('Price Reference',digits_compute=dp.get_precision('Cost Structure'),help="Price Reference"),
    'margin_reference':fields.float('Margin',digits_compute=dp.get_precision('Cost Structure'),help="Price Margin"),
    'company_id':fields.many2one('res.company','Company'),
    }
    
    _rec_name = 'unit_price'
    
    _defaults = {
    'company_id':lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid,'cost.structure', context=c),
    
    }
    
method_price()