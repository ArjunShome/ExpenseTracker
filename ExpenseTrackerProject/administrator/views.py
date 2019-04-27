from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from administrator.ReadAndUploaddb import ImportExcelAndLoad
from administrator.Static.Templates import DbTemplates

# Create your views here.
def index(request):
    return HttpResponse("Hi, This is learning of Django")

def Read_Excel_LoadDB(request):
    load = ImportExcelAndLoad()
    load.LoadExcel_ToDb()
    return HttpResponse("Congrats, you just Read Excel Sheet and Loaded the DB, Please check you db.")

def Read_Json(request):
    dic_data = {
        "name":"Arghadeep",
        "Age":"99",
        "Work":"IBM"
    }
    return JsonResponse(dic_data)

def GetDataFromDB(request):
    obj = ImportExcelAndLoad()
    data = obj.GetRecords_FromDB()
    return JsonResponse(data)

    