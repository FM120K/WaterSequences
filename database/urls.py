"""database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fm120k_db import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sampleList/', views.sampleList.as_view(), name='sampleList'),
    path('detail/<int:sample_id>', views.sample_detail, name="sample_detail"),
    path('http://127.0.0.1:8000/sampleList/addWaterSample', views.SampleCreate.as_view(), name="sample-create")
]
