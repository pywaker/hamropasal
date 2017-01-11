from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_on', 'updated_on', 'category')
    list_filter = ('name',)
    fields = ('name', 'description', 'category')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
