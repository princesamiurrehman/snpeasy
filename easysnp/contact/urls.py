from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('addrecord/', views.addrecord, name='addrecord'),
]