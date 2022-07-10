from django.contrib import admin
from .models import  Cart, Category, Product, Order, Article

from django import forms

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
    list_display = ('name', 'city', 'country', 'date_added')


admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
admin.site.register(Cart)






# for ajax


class ArticleForm(forms.ModelForm):
    
    # def __init__(self, *args, **kwargs):
    #     super(ArticleForm, self).__init__(*args, **kwargs)
    #     ## add a "form-control" class to each form input
    #     ## for enabling bootstrap
    #     for name in self.fields.keys():
    #         self.fields[name].widget.attrs.update({
    #             # 'class': 'form-control',
    #             'type': 'hidden'
    #         })
    quantity  = forms.CharField(widget=forms.HiddenInput())
    user  = forms.CharField(widget=forms.HiddenInput())
    product  = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Article
        fields = ("__all__")
        # widgets={'title': forms.HiddenInput()}
            
    
    
    
    
admin.site.register(Article)



