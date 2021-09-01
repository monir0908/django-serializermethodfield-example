from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/supplier/', include('supplier.urls')),
    path('api/merchant/', include('merchant.urls')),
]
