from django.conf.urls import url
from .views import post_detail

app_name = 'yazarlar'

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]