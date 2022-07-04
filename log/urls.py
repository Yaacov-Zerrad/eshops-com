from django.urls import path
from .views import activate, index, login_user, register, logout_user

app_name='log'
urlpatterns = [
    path('', login_user , name='login'),
    path('register', register , name='register'),
    path('login/', login_user , name='login'),
    path('logout/', logout_user , name='logout'),
    path('activate/<uidb64>/<token>/', activate , name='activate'),
]