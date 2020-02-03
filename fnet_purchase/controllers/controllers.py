# -*- coding: utf-8 -*-
from odoo import http

# class FnetPurchase(http.Controller):
#     @http.route('/fnet_purchase/fnet_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_purchase/fnet_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_purchase.listing', {
#             'root': '/fnet_purchase/fnet_purchase',
#             'objects': http.request.env['fnet_purchase.fnet_purchase'].search([]),
#         })

#     @http.route('/fnet_purchase/fnet_purchase/objects/<model("fnet_purchase.fnet_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_purchase.object', {
#             'object': obj
#         })