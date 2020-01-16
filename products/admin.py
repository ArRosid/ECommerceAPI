from django.contrib import admin

from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "featured", "price"]
    list_editable = ["active", "featured", "price"]
    list_filter = ["title","price"]

admin.site.register(models.Product, ProductAdmin)