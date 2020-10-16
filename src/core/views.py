from django.shortcuts import render
from django.http import JsonResponse    # To return Json file (API) not HTML


def test_view(request):
    # We want to return a json file not html page
    data = {
        'name': 'john',
        'age': 23
    }
    return JsonResponse(data)   # safe=False to pass in any datatype
