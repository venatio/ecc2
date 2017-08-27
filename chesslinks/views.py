from django.shortcuts import render




from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.


#def contact_list(request):
#    contact_list = Contact.objects.all()
#    return render_to_response('contacts.html', {'contact_list': contact_list})
# Create your views here.

#test view

def links(request):
    category_list = Category.objects.all()
    template = loader.get_template('links.html')

    context = {'category_list': category_list,}
    return HttpResponse(template.render(context, request))    