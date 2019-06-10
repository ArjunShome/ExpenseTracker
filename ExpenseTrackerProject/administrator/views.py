from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api import DbTemplates

# Create your views here.
paramlst = ['Date','Item','Amount']
paramdict = {}

def HomeDetails(request):
    return render(request,r'D:\MyRepo\ExpenseTracker\ExpenseTrackerProject\Templates\administrator\detail.html',{'data':DbTemplates.PopulateHome()})
    # return render(request,r'D:\MyRepo\ExpenseTracker\ExpenseTrackerProject\Templates\administrator\detail.html',{'data':'ARJUN'})

def GetYearData(request):
    paramdict.update(request.GET.get('Year'))
    data = DbTemplates.DeriveQuery(paramdict)
    return JsonResponse(data)

def GetParameters(request):
    for param in paramlst:
        paramdict.update({param:request.GET.get(param)})
    #return HttpResponse("CHECK CONSOLE, {}".format(DbTemplates.GetRecords_FromDB(paramdict)))
    return render(request,r'D:\MyRepo\ExpenseTracker\ExpenseTrackerProject\Templates\administrator\detail.html',DbTemplates.DeriveQuery(paramdict))
    