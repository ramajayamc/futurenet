# -*- coding: utf-8 -*-
from odoo import http

# class FnetTransfer(http.Controller):
#     @http.route('/fnet_transfer/fnet_transfer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_transfer/fnet_transfer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_transfer.listing', {
#             'root': '/fnet_transfer/fnet_transfer',
#             'objects': http.request.env['fnet_transfer.fnet_transfer'].search([]),
#         })

#     @http.route('/fnet_transfer/fnet_transfer/objects/<model("fnet_transfer.fnet_transfer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_transfer.object', {
#             'object': obj
#         })