from django.urls import path
from . import views

urlpatterns = [
    path('', views.ncbi, name='ncbi'),
    path('actor/', views.actor),
    path('actor/idinfo/', views.idinfo),
    path('actor/id_txt/', views.id_txt, name='id_txt'),
    path('actortwo/', views.actortwo),
    path('actorsix/', views.actorsix)
]