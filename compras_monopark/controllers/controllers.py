# -*- coding: utf-8 -*-
from odoo import http

# class ComprasMonopark(http.Controller):
#     @http.route('/compras_monopark/compras_monopark/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compras_monopark/compras_monopark/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('compras_monopark.listing', {
#             'root': '/compras_monopark/compras_monopark',
#             'objects': http.request.env['compras_monopark.compras_monopark'].search([]),
#         })

#     @http.route('/compras_monopark/compras_monopark/objects/<model("compras_monopark.compras_monopark"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compras_monopark.object', {
#             'object': obj
#         })