from django.contrib import admin

from .models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('name', 'price', 'added_on')
    search_fields = ('name', 'price', 'body')
    prepopulated_fields = {'slug': ('name',), }
    date_hierarchy = 'added_on'
    ordering = ['-added_on']


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',), }
    ordering = ['-ordering']


admin.site.register(Category, CategoryAdmin)