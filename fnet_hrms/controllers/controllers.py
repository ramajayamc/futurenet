# -*- coding: utf-8 -*-
from odoo import http

# class FnetHrms(http.Controller):
#     @http.route('/fnet_hrms/fnet_hrms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_hrms/fnet_hrms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_hrms.listing', {
#             'root': '/fnet_hrms/fnet_hrms',
#             'objects': http.request.env['fnet_hrms.fnet_hrms'].search([]),
#         })

#     @http.route('/fnet_hrms/fnet_hrms/objects/<model("fnet_hrms.fnet_hrms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_hrms.object', {
#             'object': obj
#         })