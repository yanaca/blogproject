from django.conf.urls import url
from . import views

#此处blog相当于是命名空间，它是为了区分当前url中的name与其他模块中url的name
app_name = 'blog'

#(?P<pk>[0-9]+) 表示命名捕获组 实际传递时 detail(request, pk=xxx)
urlpatterns =  [ 
    url(r'^$', views.IndexView.as_view(), name='index'), #views.index
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'), #views.detail
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'), #views.archives
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'), #views.category
 ]
