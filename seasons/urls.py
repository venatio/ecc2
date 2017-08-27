from django.conf.urls import url

from . import views

urlpatterns = [

    
    url(r'^$', views.Index, name='seasons'),
    url(r'^index/$', views.Index, name='seasons'),
    url(r'^FixtureList/$', views.FixtureList, name='seasons'),
    url(r'^Next5Fixtures/$', views.Next5Fixtures, name='seasons'),
    url(r'^about/$', views.about, name='seasons'),
    url(r'^puzzles/$', views.puzzles, name='puzzles'),
    url(r'^last5results/$', views.Last5Results, name='seasons'),
    url(r'^matchresult/(?P<pFixture>\d+/$)', views.MatchResult, name='seasons'),]

