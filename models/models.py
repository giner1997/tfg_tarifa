# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tfgtarifa(models.Model):
    _inherit = 'res.partner'

    prueba = fields.Char(string='Prueba texto', default='Álvaro')


