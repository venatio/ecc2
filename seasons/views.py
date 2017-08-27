from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime

from .models import *
from .forms import FixtureForm

#def fixturelist(request):
#    if request.method == 'POST':
#        team_str = request.POST['team']
#        if team_str == "*":
#            fixture_list = Fixture.objects.filter(campaign__season__name =request.POST['season']).order_by('date')
#        else:
#            fixture_list = Fixture.objects.filter(campaign__team__code =request.POST['team'], campaign__season__name =request.POST['season']).order_by('date')
#        form = FixtureForm(request.POST)
#    else:
#        form = FixtureForm()
#        fixture_list = Fixture.objects.filter(campaign__season__name ='16/17').order_by('date')
#   return render_to_response('seasons/fixturelist.html', {'fixture_list': fixture_list,'form': form})

def Last5Results(request,):
    fixture_list = Fixture.objects.filter(date__lte = datetime.now() , our_score__gte=0).order_by('-date')[:5]
    template = loader.get_template('last5results.html')
    context = {'fixture_list': fixture_list,}
    return HttpResponse(template.render(context, request))

def Next5Fixtures(request):
    fixture_list = Fixture.objects.filter(date__gte = datetime.now() ).order_by('date')[:5]
    template = loader.get_template('Next5Fixtures.html')
    context = {'fixture_list': fixture_list,}
    return HttpResponse(template.render(context, request))

def MatchResult(request,pFixture):
    vTitle = "Welcome to Ealing Chess CLub"
    iFixture = int(pFixture.replace('/',''))
    fixture = Fixture.objects.get(id = iFixture)
    result_list = Result.objects.filter(fixture__id = iFixture).order_by('board')

    template = loader.get_template('matchresult.html')
    context = {'result_list': result_list, 'fixture': fixture,}
    return HttpResponse(template.render(context, request))

def about(request,):
    context = {'Welcome to Ealing Chess CLub':'Title',}
    template = loader.get_template('about.html')        
    return HttpResponse(template.render(context, request))

def Index(request,):
    vTitle = "Welcome to Ealing Chess CLub"
    template = loader.get_template('home.html')
    context = {'Welcome to Ealing Chess CLub':'Title',}            
    return HttpResponse(template.render(context, request))

def puzzles(request,):
    vTitle = "Welcome to Ealing Chess CLub"
    template = loader.get_template('puzzles.html')
    context = {'Welcome to Ealing Chess CLub':'Title',}            
    return HttpResponse(template.render(context, request))

def FixtureList(request):
    if request.method == 'POST':
        team_str = request.POST['team']
        if team_str == "*":
            fixture_list = Fixture.objects.filter(campaign__season__name =request.POST['season']).order_by('date')
        else:
            fixture_list = Fixture.objects.filter(campaign__team__code =request.POST['team'], campaign__season__name =request.POST['season']).order_by('date')
        form = FixtureForm(request.POST)
    else:
        form = FixtureForm()
        fixture_list = Fixture.objects.filter(campaign__season__name ='16/17').order_by('date')
    return render(request, 'fixturelist.html', {'fixture_list': fixture_list,'form': form})
