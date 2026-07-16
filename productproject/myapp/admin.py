from django.contrib import admin
from myapp.models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=['pname','price','ptype','p_mgf','p_exp']
admin.site.register(Products,ProductsAdmin)
