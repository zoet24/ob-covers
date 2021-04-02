from django.contrib import admin
from .models import Product, Range, Style, Colour

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'range',
        'style',
        'colour',
        'price',
        'image',
    )

    ordering = ('sku',)


class RangeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ColourAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Range, RangeAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Colour, ColourAdmin)
