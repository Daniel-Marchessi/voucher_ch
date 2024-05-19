from datetime import datetime

from odoo import fields, models,api
from odoo.exceptions import UserError

import logging
class Cupon(models.Model):
    _name = 'dm.cupon'

    name        = fields.Char(string="Nombre")
    empresa_id  = fields.Many2one('res.partner',string="Empresa")
    vaucher_ids = fields.One2many('dm.cupon.vaucher', string="usuarios", inverse_name="cupon_id")
    cantidad = fields.Integer(string="Cantidad disponible", compute="compute_cantidad_disp", store=True)
    categoria_id = fields.Many2one('dm.categoria', string="Categoria")

    @api.depends('cantidad', 'vaucher_ids.estado')
    def compute_cantidad_disp(self):
        for rec in self:
         logging.info('---rec')
         logging.info(rec)
         rec.cantidad = len(rec.vaucher_ids.filtered(lambda v: v.estado == 'activo'))


    def wizard_cupon(self):
        if self.id == False:
            raise UserError("Guarde el cupon y luego podra generar vouchers")

        view = self.env.ref('voucher_ch.cupon_wz_view')
        return {
            'name': 'Cantidad de vouchers',
            'type': 'ir.actions.act_window',
            'res_model': 'wz.cupon',
            'views': [(view.id, 'form')],
            'target': 'new',
            'context': {
                'default_cupon_id': self.id
                }

        }