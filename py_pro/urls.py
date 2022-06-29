"""py_pro URL Configuration

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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.admin import OTPAdminSite
from main import models as main
from main.sitemaps import StaticViewsSitemap
from django.contrib.sitemaps.views import sitemap


 
    


class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdmin(name="OTPAdmin")

admin_site.register(User)
admin_site.register(TOTPDevice)


sitemaps = {

    'sitemap': StaticViewsSitemap
}

urlpatterns = [
    path('django_admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('',include('main.urls',namespace="main")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)