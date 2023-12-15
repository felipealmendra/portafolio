"""portafolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import view
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.index, name="index"),
    path('mail/', view.mail, name='Mail'),
    path('base/', view.base, name='Base'),
    path('portfolio/mail/', view.portfolio_mail_view, name='portfolio.mail'),
    path('prueba/', view.prueba, name='Prueba'),
    path('download/', view.download_apk, name='download_apk'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
