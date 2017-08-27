from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage


# Create your views here.
#def latest5news(request,):
#    news_list = Entry.objects
#    context = {'news_list': news_list}
#    template = loader.get_template('latest5news.html')
#    vContent = "This is quality content"
#	    #t = get_template('base.html')
#	    #return render_to_response('news/Latest5news.html', locals())
#    return HttpResponse(template.render(context, request))
 
def Index(request,):
    entry_list = Entry.objects.all().order_by('-create_date').exclude(publish='N')
    paginator=Paginator(entry_list,10)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        entry = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entry = paginator.page(paginator.num_pages)
    
    context = {'entry':entry}
    template = loader.get_template('index.html')
    #return render_to_response('news/news.html', {"entry": entry})
    return HttpResponse(template.render(context, request))

def newsitem(request,pnewsitem):
    vTitle = "Welcome to Ealing Chess CLub"
    inewsitem = int(pnewsitem.replace('/',''))
    newsitem = Entry.objects.get(id = inewsitem)
    template = loader.get_template('newsitem.html')
    context = {'newsitem':newsitem}
    #template = loader.get_template('newsitem.html')
    #return render_to_response('news/newsitem.html', locals())
    return HttpResponse(template.render(context, request))

