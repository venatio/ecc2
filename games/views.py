from django.shortcuts import render
from django.template import loader
from django.template.loader import get_template
from django.http import HttpResponse
from .models import *

# Create your views here.
def gameslist(request,):
    vTitle = "Welcome to Ealing Chess CLub"
    template = loader.get_template('gameslist.html')
    games_list = Game.objects.order_by('id')
    context = {'games_list':games_list}
    #return render_to_response('games/gameslist.html',{'games_list': games_list})
    return HttpResponse(template.render(context, request))

def game(request,pGame):
    #vTitle = "Welcome to Ealing Chess CLub"
    #t = get_template('base.html')
    iGame = int(pGame.replace('/',''))
    game = Game.objects.get(id = iGame)
    games_list = Game.objects.order_by('id')
    template = loader.get_template('game.html')
    context = {'game':game, 'games_list':games_list}
    return HttpResponse(template.render(context, request))
    #return render_to_response('games/games.html', locals())