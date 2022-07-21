from django.urls import path

from messaging.views import contact_response_auto, contact_success, contact_view

app_name='messaging'
urlpatterns = [
    path('contact_view', contact_view, name='contact_view'),
    path('contact_response_auto', contact_response_auto, name='contact_response_auto'),
    path('contact_success', contact_success, name='contact_success'),
    ]