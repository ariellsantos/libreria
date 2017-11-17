# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from . import Autor
from . import Categoria

class Libro(models.Model):
    isbn = models.CharField(max_length=150)
    nombre = models.CharField( max_length=100)
    anio = models.CharField(max_length=4)
    numero_paginas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    class Meta():
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
    
    def __unicode__(self):
        return self.nombre
    