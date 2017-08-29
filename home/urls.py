from django.conf.urls import url
from .views import *


app_name = 'home'

urlpatterns = [

    url(r'^index/', index_view(), name='index'),

]