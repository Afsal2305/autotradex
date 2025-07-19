from django.urls import path
from . import views

urlpatterns = [
    path('sell/', views.sell_vehicle, name='sell_vehicle'),
    path('buy/', views.buy_vehicle, name='buy_vehicle'),
]
