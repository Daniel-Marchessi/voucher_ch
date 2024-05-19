from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    apellido = fields.Char(string="Apellido")
    provincia = fields.Char(string="Provincia")

    cupones_ids = fields.Many2many('dm.cupon', string="Cupones")