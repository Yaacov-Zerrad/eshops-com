from django.contrib import admin
from .models import Category, Product, Order

admin.site.site_header ="E-shops"
admin.site.site_title = "YY shops"
admin.site.index_title = "manager"
class AdminCategory(admin.ModelAdmin):
    """for look in admin"""
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'Category', 'date_added')
    search_fields = ('title', 'price',)
    list_editable = ( 'price',)
    
class AdminOrder(admin.ModelAdmin):
    list_display = ('name','total', 'city', 'country', 'date_added')


admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
