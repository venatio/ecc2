from seasons.models import *
#from ecc.News.models import *

from django import template
from datetime import datetime

register = template.Library()

@register.inclusion_tag('next5fixtures.html')
def next5fixtures():
    fixture_list = Fixture.objects.filter(date__gte = datetime.now ).order_by('date')[:5]
    return {'fixture_list': fixture_list}
    
@register.inclusion_tag('last5results.html')
def last5results():
    fixture_list = Fixture.objects.filter(date__lte = datetime.now , our_score__gte=0).order_by('-date')[:5]
    
    return {'fixture_list': fixture_list,} 

 
#@register.inclusion_tag('news/latest5news.html')
#def latest5news():
#    news_list = Entry.objects.filter().order_by('-create_date')[:5]
#    return {'news_list': news_list}   

@register.inclusion_tag('latest5matchreports.html')
def latest5matchreports():
    fixture_list = Fixture.objects.filter(date__lte = datetime.now, our_score__gte=0).order_by('-date')[:5]
    return {'fixture_list': fixture_list}    
