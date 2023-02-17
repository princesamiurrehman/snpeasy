from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

@csrf_exempt
def addrecord(request):
    a = request.POST['first']
    b = request.POST['last']
    c = request.POST['email']
    d = request.POST['comments']
    e = request.POST['checkbox']
    contact = Contact(firstname=a, lastname=b, emailaddress=c, comments=d, checkbox=e)
    contact.save()
    return HttpResponseRedirect(reverse('contact'))

