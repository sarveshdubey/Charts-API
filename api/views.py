from django.shortcuts import render, HttpResponse
from api.models import stocks
import requests
import json

# Create your views here.


def index(request):
    if request.method =="POST":
        symbol=request.POST.get('symbol',None)
        print()
        url='https://docker.api.srifintech.com/testassignment'

        data = {   
        "ticker": symbol
            }
        r = requests.post(url = url, data = data)

        something = r.json()
        param = {
            'strike':something['strike'],
            'calloi':something['calloi'],
            'putoi':something['putoi'],
        }
        series = []
        for key, values in something.items():
            temp = {}
            if key == "strike":
                continue
            temp["name"] = key
            temp["data"]= values
            series.append(temp)
        # print(series)
        print("-----------------------------------------")
        chart = {
                'chart': {'type': 'bar'},
                'title': {'text': 'Open Interests'}
                }
        chart["series"] = series
        print(chart)
        dump = json.dumps(chart)
        return render(request,'index.html',{'param':param, 'chart': dump})
    return render(request,'index.html')

