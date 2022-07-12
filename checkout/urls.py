from django.urls import path
from checkout import views

app_name='check'
urlpatterns = [
    path('deliverychoices/', views.deliverychoices, name='deliverychoices'), 
    path("basket_update_delivery/", views.cart_update_delivery, name="cart_update_delivery"),
    path("delivery_address/", views.delivery_address, name="delivery_address"),
    path("payment_selection/", views.payment_selection, name="payment_selection"),
    path("payment_complete/", views.payment_complete, name="payment_complete"),
    path("payment_successful/", views.payment_successful, name="payment_successful"),
]