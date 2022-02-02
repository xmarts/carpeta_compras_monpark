# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
	_inherit = "purchase.order"

	compra_tipo = fields.Selection(selection=[('nacional', 'Nacional'),('internacional', 'Internacional')], string="Tipo de compra")
	prueba = fields.Char(string="Referencia interna")
	desea_ref_banco = fields.Boolean(string="Desea agregar la referencia del banco", default=False)
	ref_banco = fields.Char(string="Referencia del banco")
	fecha_prevista = fields.Datetime(related="write_date", string="Fecha prevista")
	name = fields.Char('Pedir referencia', required=True, index=True, copy=False, default='Nuevo')

	@api.onchange('partner_ref')
	def _function_factura(self):
		for record in self:
			if record.partner_ref:
				if record.partner_ref != "":
					obj_pur_order = self.env['purchase.order'].search([('partner_ref', '=', self.partner_ref)])
					if obj_pur_order:
						raise ValidationError('La factura de proveedor ' + self.partner_ref + ' ya esta registrada para el mismo proveedor.')
						


class PurchaseOrderLine(models.Model):
	_inherit = "purchase.order.line"

	imagen_producto = fields.Binary(compute="_get_imagen")

	@api.onchange('product_id')
	def _get_imagen(self):
		for line in self:
			if line.product_id:
				line.imagen_producto = line.product_id.image_512

class AccountIncoterms(models.Model):
	_inherit  = 'account.incoterms'

	@api.model
	def name_get(self):
		result = []
		for record in self:
			record_name = str(record.code)
			result.append((record.id, record_name))
		return result