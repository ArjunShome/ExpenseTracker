from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeDetails, name = 'Home'),
    path(r'?Year=(\d{3}+)',views.GetYearData, name = 'YearWiseData'),
    path('getdbdataJson/',views.GetParameters, name = 'GetParameters')
] 
