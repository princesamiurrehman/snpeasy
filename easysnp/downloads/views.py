from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def downloads(request):
    template = loader.get_template('downloads.html')
    return HttpResponse(template.render())