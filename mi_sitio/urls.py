from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app1/', include('mi_app1.urls')),
    path('mi_app2/', include('mi_app2.urls')),
]


        



