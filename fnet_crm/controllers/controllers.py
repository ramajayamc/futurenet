# -*- coding: utf-8 -*-
# from odoo import http


# class FnetCrm(http.Controller):
#     @http.route('/fnet_crm/fnet_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_crm/fnet_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_crm.listing', {
#             'root': '/fnet_crm/fnet_crm',
#             'objects': http.request.env['fnet_crm.fnet_crm'].search([]),
#         })

#     @http.route('/fnet_crm/fnet_crm/objects/<model("fnet_crm.fnet_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_crm.object', {
#             'object': obj
#         })
