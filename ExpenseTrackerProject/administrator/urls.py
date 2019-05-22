from django.urls import path
from . import views

urlpatterns = [
    path('getdbdataJson/',views.GetParameters, name = 'GetParameters')
] 
