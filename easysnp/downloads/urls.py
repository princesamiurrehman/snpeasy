from django.urls import path
from . import views

urlpatterns = [
    path('', views.downloads, name='downloads'),
]