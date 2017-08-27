from django.conf.urls import url

from . import views

urlpatterns = [

    

    url(r'^$', views.Index, name='seasons'),
    url(r'^newsitem/(?P<pnewsitem>\d+/$)', views.newsitem, name='seasons'),]