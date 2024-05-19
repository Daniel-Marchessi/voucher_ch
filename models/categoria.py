from odoo import fields,models

class Categoria(models.Model):
    _name = 'dm.categoria'

    name = fields.Char(string="Nombre")