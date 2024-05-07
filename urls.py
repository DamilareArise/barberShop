"""
URL configuration for barberShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from barberShop.userApp.views import SignUpView
from barberShop.serviceApp.views import index
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),
    path('price/', TemplateView.as_view(template_name='price.html'), name='price'),
    # path('service/', TemplateView.as_view(template_name='service.html'), name='service'),
    path('single/', TemplateView.as_view(template_name='single.html'), name='single'),
    path('team/', TemplateView.as_view(template_name='team.html'), name='team'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name="signup"),
    re_path(r'^userApp/', include('barberShop.userApp.urls')),
    re_path(r'^serviceApp/', include('barberShop.serviceApp.urls'))

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)