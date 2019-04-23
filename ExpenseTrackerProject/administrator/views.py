from django.shortcuts import render
from django.http import HttpResponse
from administrator.readAndUpload import importExcelAndLoad

# Create your views here.
def index(request):
    return HttpResponse("Hi, This is learning of Django.")

def dbUpload(request):
    importExcelAndLoad.importExcel()
    return HttpResponse("Congrats :), Database got updated with the latest Expense records.")