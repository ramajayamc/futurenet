# -*- coding: utf-8 -*-
from odoo import http

# class FnetFunnel(http.Controller):
#     @http.route('/fnet_funnel/fnet_funnel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_funnel/fnet_funnel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_funnel.listing', {
#             'root': '/fnet_funnel/fnet_funnel',
#             'objects': http.request.env['fnet_funnel.fnet_funnel'].search([]),
#         })

#     @http.route('/fnet_funnel/fnet_funnel/objects/<model("fnet_funnel.fnet_funnel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_funnel.object', {
#             'object': obj
#         })