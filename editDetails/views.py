from django.shortcuts import render
import requests
import json

def editDetailsPageView(request):
    api_url = ""
    context = {
        "api_url" : api_url

    }
    return render(request, 'searchFood/searchFood.html',context)
# Create your views here.


def searchfood(request):
    query = request.POST['query']
    api_url = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=nKJziBX85O1PlauEx7zsd6qI5zlI4mWcF6aP3ODx&query=" + query + "&pageSize=10&dataType=Survey (FNDDS)"
    response = requests.get(api_url)
    json_data = json.loads(response.text)
    data_dict = dict()
    dict_outer = dict()
    
    listdict = []
    data_dict['Name'] = json_data['foods'][0]['description']

    for entry in json_data['foods'][0]['foodNutrients']:
        name = entry['nutrientName']
        unit = entry['unitName']
        amount = entry['value']

        if name == 'Protein':
            data_dict['Protein'] = [amount,unit]
        elif name == 'Water':
            data_dict['Water'] = [amount,unit]
        elif name == 'Water':
            data_dict['Phosphorus, P'] = [amount,unit]
        elif name == 'Potassium, K':
            data_dict['Pho'] = [amount,unit]
        elif name == 'Sodium, Na':
            data_dict['Na'] = [amount,unit]


    # test = json_data['foods'][0]['foodNutrients'][0]['nutrientName']
    test = json_data['foods'][0]['foodNutrients']

       
    context = {
        "api_url" : api_url,
        "test" : data_dict,
        "name" : data_dict['Name'],
        "header" : ["", "Name","Protein","Water","Phosphorus"],
        "proteinval": data_dict['Protein'][0],
        "proteinunit": data_dict['Protein'][1],
        "waterval": data_dict['Water'][0],
        "waterunit": data_dict['Water'][1],
        "phosval": data_dict['Pho'][0],
        "phosunit": data_dict['Pho'][1],
    }

    return render(request, 'searchFood/searchFood.html', context)