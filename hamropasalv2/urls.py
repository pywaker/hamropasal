"""hamropasalv2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from category.views import home_page, products, contact

import category.views as cviews


urlpatterns = [
    url(r'^$', cviews.home_page, name='homepage'),
    url(r'^category/(?P<category_id>[0-9]+)', cviews.products, name='products'),
    url(r'^contact/', cviews.contact, name='contact'),
    url(r'^category/add', cviews.add_category, name='add_category'),
    url(r'^admin/', admin.site.urls),
]
