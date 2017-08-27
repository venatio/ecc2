#from django.shortcuts import render


from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.


#def contact_list(request):
#    contact_list = Contact.objects.all()
#    return render_to_response('contacts.html', {'contact_list': contact_list})
# Create your views here.

#test view

def index(request):
    contact_list = Contact.objects.all()
    template = loader.get_template('contacts.html')

    context = {'contact_list': contact_list,}
    return HttpResponse(template.render(context, request))