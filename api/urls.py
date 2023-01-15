from django.urls import path
from .views import GetStockData, AllStocks

urlpatterns = [
    path('stocks/', AllStocks.as_view()),
    path('<str:tikr>/', GetStockData.as_view()),
]
