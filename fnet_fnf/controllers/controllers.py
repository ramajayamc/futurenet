# -*- coding: utf-8 -*-
from odoo import http

# class FnetFnf(http.Controller):
#     @http.route('/fnet_fnf/fnet_fnf/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_fnf/fnet_fnf/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_fnf.listing', {
#             'root': '/fnet_fnf/fnet_fnf',
#             'objects': http.request.env['fnet_fnf.fnet_fnf'].search([]),
#         })

#     @http.route('/fnet_fnf/fnet_fnf/objects/<model("fnet_fnf.fnet_fnf"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_fnf.object', {
#             'object': obj
#         })