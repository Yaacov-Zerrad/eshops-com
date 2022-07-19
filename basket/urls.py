from django.urls import path

from basket.views import basket_view, basket_add, basket_delete, basket_dimin, basket_page, basket_json
app_name='basket'
urlpatterns = [
    path('', basket_view, name='basket_view' ),
    path('basket_page', basket_page, name='basket_page' ),
    path('basket_add', basket_add, name='basket_add' ),
    path('basket_dimin', basket_dimin, name='basket_dimin' ),
    path('basket_delete', basket_delete, name='basket_delete' ),
    path('basket_json', basket_json, name='basket_json' ),
]