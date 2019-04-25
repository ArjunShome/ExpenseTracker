from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index, name = 'index'),
    path('dbinsert/',views.Read_Excel_LoadDB, name = 'dbinsert')
] 
