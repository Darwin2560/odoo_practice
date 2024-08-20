# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school(models.Model):
    _name = 'school.student'
    _description = 'Tabla de Estudiantes'

    name = fields.Char(string="Nombre", required=True)
    age = fields.Integer(string="Edad", required=True)

