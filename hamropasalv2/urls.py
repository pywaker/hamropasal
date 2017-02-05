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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
#from category.views import home_page, products, contact
from django.views.generic import TemplateView
from rest_framework import routers

import category.views as cviews
from category.resources import ProductViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    url(r'^$', cviews.home_page, name='homepage'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^category/', cviews.CategoryAddView.as_view(), name='category'),
    #url(r'^products/', cviews.ProductAddView.as_view(), name='add_product'),
    #url(r'^category/(?P<category_id>[0-9]+)', cviews.products, name='products'),
    url(r'^contact/', cviews.contact, name='contact'),
    #url(r'^category/add', cviews.add_category, name='add_category'),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
