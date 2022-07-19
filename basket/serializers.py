from dataclasses import fields
from urllib import request
from basket.models import Basket
from rest_framework import serializers

# class BasketSerializer(serializers.ModelSerializer):
#     def __init__(self, request, *args, **kwargs):
#         super(BasketSerializer, self).__init__(*args, **kwargs)
#         self.request = request
        
#     class Meta:
#         model = Basket(request=request)
#         fields = '__all__'