from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from administrator.ReadAndUploaddb import ImportExcelAndLoad

# Create your views here.
def index(request):
    return HttpResponse("Hi, This is learning of Django")

def Read_Excel_LoadDB(request):
    load = ImportExcelAndLoad()
    load.LoadExcel_ToDb()
    return HttpResponse("Congrats, you just Read Excel Sheet and Loaded the DB, Please check you db.")

def Read_Json(response):
    dic_data = {
        "name":"Arghadeep",
        "Age":"99",
        "Work":"IBM"
    }
    return JsonResponse(dic_data)
    