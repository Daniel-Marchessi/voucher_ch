from odoo import fields, models

class Vaucher(models.Model):
    _name = 'dm.cupon.vaucher'

    name = fields.Char(string="Nombre")
    cupon_id = fields.Many2one('dm.cupon', string="Cupon")
    code = fields.Char(string="Codigo")
    empresa_id  = fields.Many2one('res.partner',string="Empresa")

    estado = fields.Selection([
        ('activo', 'Activo'),
        ('asignado', 'Asignado'),
        ('canjeado', 'Canjeado')
    ], default='activo')
    user_id = fields.Many2one('res.users', string="Usuario")
