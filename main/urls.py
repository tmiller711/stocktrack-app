from django.urls import path

from .views import homepage, documentation, dashboard

urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('documentation/', documentation, name='documentation')
]