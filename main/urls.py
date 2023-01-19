from django.urls import path

from .views import homepage, documentation, dashboard, add_credits

urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('documentation/', documentation, name='documentation'),
    path('addcredits/', add_credits, name='add_credits'),
]