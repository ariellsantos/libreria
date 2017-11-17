# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField( max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __unicode__(self):
        return self.nombre