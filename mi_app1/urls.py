# mi_app1/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_1, name='vista_1'),
    path('vista2/', views.vista_2, name='vista_2'),
]