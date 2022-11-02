from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>/', views.successMsg, name='success'),
    path('view/', views.view_all_payments, name='payment_view'),
]