from django.shortcuts import render
import requests
import json
import pprint
from datetime import datetime, timedelta, time, date


def editDetailsPageView(request):
    api_url = ""
    context = {
        "api_url" : api_url

    }
    return render(request, 'searchFood/searchFood.html',context)
# Create your views here.

# This searches the usda API to get nutrient data

def searchfood(request):
    
    # take a query and search the API
    query = request.POST['query']
    api_url = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=nKJziBX85O1PlauEx7zsd6qI5zlI4mWcF6aP3ODx&query=" + query + "&pageSize=10&dataType=Survey (FNDDS)"
    response = requests.get(api_url)
    json_data = json.loads(response.text)
    data_dict = dict()
    dict_outer = dict()
    length = len(json_data['foods'][0]['description'])
    today = datetime.today()

    # store API data to a dictionary
    listdict = []
    data_dict['Name'] = json_data['foods'][0]['description']
    fdcid = json_data['foods'][0]['fdcId']
    for entry in json_data['foods'][0]['foodNutrients']:
        name = entry['nutrientName']
        unit = entry['unitName']
        amount = entry['value']

        if name == 'Protein':
            data_dict['Protein'] = [amount,unit]
        elif name == 'Phosphorus, P':
            data_dict['Pho'] = [amount,unit]
        elif name == 'Potassium, K':
            data_dict['Potassium'] = [amount,unit]
        elif name == 'Sodium, Na':
            data_dict['Na'] = [amount,unit]

       
    context = {
        "api_url" : api_url,
        "test" : data_dict,
        "name" : data_dict['Name'],
        "header" : ["", "Name","Protein","Potassium","Phosphorus","Sodium","Quantity","Select Date"],
        "proteinval": data_dict['Protein'][0],
        "proteinunit": data_dict['Protein'][1],
        "kval": data_dict['Potassium'][0],
        "kunit": data_dict['Potassium'][1],
        "phosval": data_dict['Pho'][0],
        "phosunit": data_dict['Pho'][1],
        "naval": data_dict['Na'][0],
        "naunit": data_dict['Na'][1],
        "fdcid" : fdcid,
        "length" : length,
        "today" : today
    }

    return render(request, 'searchFood/searchFood.html', context)