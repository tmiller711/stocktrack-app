from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, date
import pandas as pd

from .models import Stock
from .serializers import StockSerializer

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
