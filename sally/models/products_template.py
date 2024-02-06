from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_flower = fields.Boolean(string='Is a Flower')
    flower_id= fields.Many2one("flower.shop")
    sequence_id = fields.Many2one('ir.sequence', string="Flower Sequence")
    gardener_id = fields.Many2one('res.users')
    needs_watering = fields.Boolean(default=False)