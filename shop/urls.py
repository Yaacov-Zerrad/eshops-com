from django.conf import settings
from django.urls import path
from .views import add_article,  add_user_article, get_data_cart, calcul, checkout, detail, index, indexajax,   templates, temdetail, add_to_cart
from django.conf.urls.static import static

app_name='shop'
urlpatterns = [
    path('', index, name='index'),
    
    path('<int:pk>', detail , name='detail'),
    path('add/<str:slug>', add_to_cart , name='add_to_cart'),
    path('checkout', checkout , name='checkout'),
    path("create_post", add_article, name="add_article"),
    path("get_data_cart", get_data_cart, name="get_data_cart"),
    
    
    path("ajax", indexajax, name="indexajax"),
    path("ww", calcul, name="calcul"),
    
    path("post_creat/", add_user_article, name="add_user_article"),
    path('tem', templates, name='templates'),
    path('temdetail', temdetail, name='temdetail'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)