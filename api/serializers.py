from rest_framework import serializers
from .models import Stock
from django.contrib.auth import get_user_model

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock 
        fields = ('ticker', 'stock_data')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
