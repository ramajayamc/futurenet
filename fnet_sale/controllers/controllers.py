# -*- coding: utf-8 -*-
from odoo import http

# class FnetSale(http.Controller):
#     @http.route('/fnet_sale/fnet_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_sale/fnet_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_sale.listing', {
#             'root': '/fnet_sale/fnet_sale',
#             'objects': http.request.env['fnet_sale.fnet_sale'].search([]),
#         })

#     @http.route('/fnet_sale/fnet_sale/objects/<model("fnet_sale.fnet_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_sale.object', {
#             'object': obj
#         })