# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('calculate-price/<int:vehicle_id>/', views.calculate_final_price, name='calculate-price'),
]
