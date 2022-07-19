from django.urls import path

from customuser.views import address_default, address_form, address_list,address_delete, address_update, address_view


app_name='customuser'
urlpatterns = [
    path('address_form', address_form, name='address_form'),        
    path('address_view', address_view, name='address_view'),        
    path('address_list', address_list, name='address_list'),        
    path('address_update/<int:pk>', address_update, name='address_update'),        
    path('address_delete/<int:pk>', address_delete, name='address_delete'),        
    path('address_default/<int:pk>', address_default, name='address_default'),        
    ]