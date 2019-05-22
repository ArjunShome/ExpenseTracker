from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api import DbTemplates

# Create your views here.
paramlst = ['Date','Item','Amount']
paramdict = {}

def GetParameters(request):
    for param in paramlst:
        paramdict.update({param:request.GET.get(param)})
    #return HttpResponse("CHECK CONSOLE, {}".format(DbTemplates.GetRecords_FromDB(paramdict)))
    return render(request,r'D:\MyRepo\ExpenseTracker\ExpenseTrackerProject\Templates\administrator\detail.html',DbTemplates.GetRecords_FromDB(paramdict))
    