from django.shortcuts import render
from django.http import JsonResponse

# Third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post


class TestView(APIView):
    """
    By using a classbased view and ingeriting from APIView gives us a lot of methods to work with.
    """
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # serializing a qs of a model so no need for validating
        # Serializeing multiple elements
        serializer = PostSerializer(qs, many=True)
        
        # serializing single element
        #post = qs.first()
        #serializer = PostSerializer(post)
        return Response(serializer.data)

    # By defining this post method, the view can handle POST request
    def post(self, request, *arg, **kwargs):
        # When passing a data, it means we want to check if data is valid. 
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)