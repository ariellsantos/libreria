# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from . import Libro

class Prestamo(models.Model):
    ESTATUS = (
        ('a', 'Activo'),
        ('c', 'Cerrado')
    )

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    estatus = models.CharField(max_length=8, choices=ESTATUS, default='a')

    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"

    
    def __unicode__(self):
        return "Nombre libro: {} Usuario: {} Estatus:".format(self.libro , self.usuario, self.estatus)
