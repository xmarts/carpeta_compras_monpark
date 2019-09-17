# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
	_inherit = "purchase.order"

	compra_tipo = fields.Selection(selection=[('nacional', 'Nacional'),('internacional', 'Internacional')], string="Tipo de compra")
	prueba = fields.Char(string="Referencia interna")

class PurchaseOrderLine(models.Model):
	_inherit = "purchase.order.line"

	imagen_producto = fields.Binary(compute="_get_imagen")


	@api.depends('product_id')
	def _get_imagen(self):
		for line in self:
			if line.product_id:
				line.imagen_producto = line.product_id.image_medium