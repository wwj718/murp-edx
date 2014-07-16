from django.conf.urls import patterns, url
from .views import murp_home,murp_hello

urlpatterns = patterns('',
                       (r'^hello$', murp_hello),
                       )
