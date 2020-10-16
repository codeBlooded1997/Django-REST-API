from django.shortcuts import render
from django.http import JsonResponse    # To return Json file (API) not HTML

# Third party imports
from rest_framework.response import Response    # What we return (Inherits from JsonResponse)
from rest_framework.views import APIView    # Allows to create a view that accept cerain types of requests(get, post, ...)


class TestView(APIView):
    """
    By using a classbased view and ingeriting from APIView gives us a lot of methods to work with.
    """
    def get(self, request, *args, **kwargs):
        # This get method is used when someone sends a get request to this end-pont and we use Response to return response at the end of this request.
        data = {
            'name': 'john',
            'age': 23
        }

        return Response(data)

#def test_view(request):
    # We want to return a json file not html page
    #data = {
    #    'name': 'john',
    #}
    #return JsonResponse(data)   # safe=False to pass in any datatype
