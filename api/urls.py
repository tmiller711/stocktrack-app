from django.urls import path
from .views import GetStockData, AllStocks, LoginAccount, RegisterAccount, GetAccount

urlpatterns = [
    path('stocks/', AllStocks.as_view()),
    path('<str:tikr>/', GetStockData.as_view()),
    path('account/login/', LoginAccount.as_view(), name='login'),
    path('account/register', RegisterAccount.as_view(), name='register'),
    path('account/getaccount', GetAccount.as_view(), name='getaccount')
]
