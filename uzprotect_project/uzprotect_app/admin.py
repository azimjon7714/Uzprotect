from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model: Category

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model: Category

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(AboutUs)
# Register your models here.
