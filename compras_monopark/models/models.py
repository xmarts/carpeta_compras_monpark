# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
	_inherit = "purchase.order"

	compra_tipo = fields.Selection(selection=[('nacional', 'Nacional'),('internacional', 'Internacional')], string="Tipo de compra")