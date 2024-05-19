from odoo import fields,models


class ResUser(models.Model):
    _inherit = 'res.users'

    cupon_id = fields.Many2one('dm.cupon', string="cupon")