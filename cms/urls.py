from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^hh/$', views.hh_list, name='hh_list'),
    url(r'^hh/add/$', views.hh_edit, name='hh_add'),
    url(r'^hh/mod/(?P<hh_id>\d+)/$', views.hh_edit, name='hh_mod'),
    url(r'^hh/del/(?P<hh_id>\d+)/$', views.hh_del, name='hh_del'),
]