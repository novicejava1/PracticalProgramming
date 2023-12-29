from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# CVE index
cveindex = "https://fedser32.stack.com:9200/cveindex"

# Opensearch environment variables
baseurl = "https://fedser32.stack.com:9200"
username = "admin"
password = "admin"
auth = (username, password)
sslcheck = False


# Create your views here.
def index(request):
    cvecount = requests.get(cveindex + "/_count", auth=auth, verify=sslcheck)
    print(cvecount.json()['count'])
    count = cvecount.json()['count']
    return HttpResponse("CVE item count : %s" % count)

def cvedata(request):
    cvecount = requests.get(cveindex + "/_count", auth=auth, verify=sslcheck)
    print(cvecount.json()['count'])
    count = cvecount.json()['count']
    
    jsonitems = {}
    for item in range(count):
        data = requests.get(cveindex + "/_doc/" + str(item), auth=auth, verify=sslcheck)
        jsondata = data.json()
        jsonitems[item] = jsondata
    print(jsonitems)
    context = {'jsonitems': jsonitems}

    return render(request, 'cvewebapp/cvedata.html', context)
    #return HttpResponse("Hello CVEData")
