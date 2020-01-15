from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
	list_filter = ['available', 'created_at', 'updated_at']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)
