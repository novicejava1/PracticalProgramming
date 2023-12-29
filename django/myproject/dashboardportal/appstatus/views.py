from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import requests
import sys
import concurrent.futures
import os
from django.conf import settings
import time

# Create your views here.
def index(request):
    template = loader.get_template('status.html')
    return HttpResponse(template.render())

def webstatus(request):
    #apiList = ["https://riskservicesdev.momentum.co.za/riskacceptanceapi/mgmt/health", "https://riskservicesdev.momentum.co.za/risk-comms-module/mgmt/health"]
    apiList = []
    CONNECTIONS=5
    
    with open(os.path.join(settings.BASE_DIR, 'urllist.txt'), "r") as file:
        for eachurl in file:
            apiList.append(eachurl.strip())

    #print(len(apiList))
    data = {}
    #for each in apiList:
    #    res = requests.head(each)
    #    #response.append(res.status_code)
    #    #print(apiList, response.status_code)
    #    data[each] = res
    #print(data)


    def getStatus(apiList):
        response = requests.head(apiList)
        data[apiList] = response

    time1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        a = executor.map(getStatus, apiList)
    time2 = time.time()


    context = {'data': data,}
    template = loader.get_template('webstatus.html')
    return HttpResponse(template.render(context, request))


