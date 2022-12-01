import json
from django.shortcuts import render
# from .query import dictsodium, listsodium, dictk, listk
# import json
 
# # Create your views here.
def dashboardPageView(request):
#     datasodium = dictsodium
    context = {
#         'datasodium': datasodium,
#         'valuessodium': listsodium,
#         'datak' : dictk,
#         'valuesk' : listk,
    }
    return render(request, 'dashboard/dashboard.html', context)
#     print(data)

