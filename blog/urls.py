from django.conf.urls import url
from . import views

#此处blog相当于是命名空间，它是为了区分当前url中的name与其他模块中url的name
app_name = 'blog'

#(?P<pk>[0-9]+) 表示命名捕获组 实际传递时 detail(request, pk=xxx)
urlpatterns =  [ 
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
 ]
