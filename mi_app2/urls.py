from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_3, name='vista_3'),
    path('vista4/', views.vista_4, name='vista_4'),
]