from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, date
import pandas as pd
from django.contrib.auth import login, authenticate
from rest_framework.permissions import IsAuthenticated

from .models import Stock
from accounts.models import Account
from .serializers import StockSerializer, AccountSerializer

# Create your views here.

class GetStockData(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        indicator_args = request.data.get('indicators')
        start_date = datetime.strptime(request.data.get('start_date'), "%Y-%m-%d").date()
        end_date = datetime.strptime(request.data.get('end_date'), "%Y-%m-%d").date()
        
        ticker = kwargs['tikr']
        try:
            stock = Stock.objects.get(ticker=ticker)
        except:
            return Response({"Error": "Stock not found"}, status=status.HTTP_404_NOT_FOUND)

        data = pd.read_csv(stock.stock_data)
        for index, row in data.iterrows():
            # convert date string to date object
            data.at[index, 'date'] = datetime.strptime(row['date'], "%Y-%m-%d").date()

        data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

        indicators = ['date', 'open', 'close', 'high', 'low']
        for indicator in indicator_args:
            indicators.append(indicator)
        data = data[indicators]

        return Response(data, status=status.HTTP_200_OK)

class AllStocks(APIView):
    def get(self, request, format=None):
        stocks = [stock.ticker for stock in Stock.objects.all()]
        stocks = ', '.join(stocks)

        return Response(stocks, status=status.HTTP_200_OK)

class RegisterAccount(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            account = Account(email=email)
            account.set_password(password)
            account.save()
            return Response({'Account created': 'Good stuff'}, status=status.HTTP_201_CREATED)

        return Response({'error': 'creating account'}, status=status.HTTP_400_BAD_REQUEST)

class LoginAccount(APIView):
    def post(self, request, format=None):
            email = request.data.get('email')
            password = request.data.get('password')
            if len(email) > 0 and len(password) > 0:
                account = authenticate(request, email=email, password=password)
                if account is not None:
                    login(request, account)
                    return Response({'Logged': 'In'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'signing in'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'error': 'signing in'}, status=status.HTTP_400_BAD_REQUEST)

class GetAccount(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        account = Account(email=request.user.email)
        if account is not None:
            return Response({'email': account.email}, status=status.HTTP_200_OK)
        return Response({"error": "couldn't find account"}, status=status.HTTP_404_NOT_FOUND)