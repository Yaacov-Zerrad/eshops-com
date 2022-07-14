from django.urls import path

from basket.views import basket_page

app_name='basket'
urlpatterns = [
    path('', basket_page, name='basket_page' ),
]