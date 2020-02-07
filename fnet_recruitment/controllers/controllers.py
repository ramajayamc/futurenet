# -*- coding: utf-8 -*-
from odoo import http

# class FnetRecruitment(http.Controller):
#     @http.route('/fnet_recruitment/fnet_recruitment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fnet_recruitment/fnet_recruitment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fnet_recruitment.listing', {
#             'root': '/fnet_recruitment/fnet_recruitment',
#             'objects': http.request.env['fnet_recruitment.fnet_recruitment'].search([]),
#         })

#     @http.route('/fnet_recruitment/fnet_recruitment/objects/<model("fnet_recruitment.fnet_recruitment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fnet_recruitment.object', {
#             'object': obj
#         })