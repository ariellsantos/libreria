# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    def __unicode__(self):
        return self.nombre
