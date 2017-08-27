from django.conf.urls import url

from . import views

urlpatterns = [

    

    url(r'^$', views.gameslist, name='gamelist'),
    url(r'^(?P<pGame>\d+/$)', views.game, name = 'game'), 
    #url(r'^gameslist/\d+/$)', views.newsitem, name='seasons'),
    ]