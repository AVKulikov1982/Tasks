"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
	path('i18n', include('django.conf.urls.i18n')),
	path('api-auth/', include('rest_framework.urls')),
	path('', include('app_main.urls'), name='main'),
	path('', include('app_tasks.urls'), name='tasks'),
	path('', include('app_users.urls'), name='users'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)