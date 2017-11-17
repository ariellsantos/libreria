# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import  Autor, Categoria, Libro, Prestamo
# Register your models here.



@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "autor", "categoria", "disponible")

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'fecha_prestamo', 'fecha_entrega', 'estatus')