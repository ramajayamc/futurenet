# -*- coding: utf-8 -*-
from odoo import http

# class FnetSaleTargets(http.Controller):
#     @http.route('/fnet_sale_targets/fnet_sale_targets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_sale_targets/fnet_sale_targets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_sale_targets.listing', {
#             'root': '/fnet_sale_targets/fnet_sale_targets',
#             'objects': http.request.env['fnet_sale_targets.fnet_sale_targets'].search([]),
#         })

#     @http.route('/fnet_sale_targets/fnet_sale_targets/objects/<model("fnet_sale_targets.fnet_sale_targets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_sale_targets.object', {
#             'object': obj
#         })