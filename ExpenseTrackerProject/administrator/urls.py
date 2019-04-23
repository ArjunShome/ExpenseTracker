from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index, name = 'index'),
    path('read_excel/',views.Read_Excel, name = 'read_excel')
]