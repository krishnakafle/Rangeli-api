"""municipalProfile URL Configuration

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
from django.urls import path, include

from mapLayersAPI.models import Rangeli
from custom_rest_framework_mvt.views import mvt_view_factory
# from mapLayersAPI.views import ResponseApie


urlpatterns = [
    path('admin/', admin.site.urls),
    # contour line
    path("api/v1/data/municipality.mvt/", mvt_view_factory(Rangeli)),
    path('api/v1/', include('dataAPI.urls')),
    path('api/v1/layers/', include('mapLayersAPI.urls')),
    # path('kk', ResponseApie.as_view(), name='kk')
]
