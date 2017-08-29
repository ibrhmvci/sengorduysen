"""sengorduysen URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from home.views import index_view
from haberler.views import news_view
from yazarlar.views import yazar_list_view
from blog.views import blog_list_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name='index'),
    url(r'^haberler/', news_view, name='haberler'),
    url(r'^yazarlar/yazi/', include('yazarlar.urls')),
    url(r'^yazarlar/', yazar_list_view, name='yazarlar'),
    url(r'^blog/blog-detail/', include('blog.urls')),
    url(r'^blog/', blog_list_view, name='blog'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)