from importlib.resources import path
from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.persona, name='persona')
]
