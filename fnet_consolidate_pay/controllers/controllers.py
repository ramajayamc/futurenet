# -*- coding: utf-8 -*-
from odoo import http

# class FnetConsolidatePay(http.Controller):
#     @http.route('/fnet_consolidate_pay/fnet_consolidate_pay/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_consolidate_pay/fnet_consolidate_pay/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_consolidate_pay.listing', {
#             'root': '/fnet_consolidate_pay/fnet_consolidate_pay',
#             'objects': http.request.env['fnet_consolidate_pay.fnet_consolidate_pay'].search([]),
#         })

#     @http.route('/fnet_consolidate_pay/fnet_consolidate_pay/objects/<model("fnet_consolidate_pay.fnet_consolidate_pay"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_consolidate_pay.object', {
#             'object': obj
#         })