from django.urls import path
from . import views

urlpatterns = [
    path('', views.departamento, name='departamento'),
]
