from datetime import datetime

from odoo import fields, models, api, _
import logging

class ResConfigSettings(models.TransientModel):
    _name = 'wz.cupon'

    cantidad = fields.Integer(string="Cantidad")
    cupon_id = fields.Many2one('dm.cupon', string="Cupon")
    def create_vouchers(self):
        vat = self.cupon_id.empresa_id.vat
        logging.info('-------d')
        logging.info(vat)

        mes = datetime.now().strftime('%m')

        for rec in range(self.cantidad):
            code = self.env['ir.sequence'].next_by_code('dm.cupon.vaucher')
            logging.info('--Code --')
            logging.info(code)
            cupon_code = f'{vat}-{mes}-{code}'
            vaucher = self.env['dm.cupon.vaucher'].create({

                'name': self.cupon_id.name,
                'cupon_id': self.cupon_id.id,
                'code': cupon_code,
                'empresa_id': self.cupon_id.empresa_id.id,

            })
        logging.info('-------test')

