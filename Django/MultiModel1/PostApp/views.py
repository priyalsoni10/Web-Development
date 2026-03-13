# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PostModel
from .serializer import PostViewSerializer
from .serializer import PostCreateSerializer


# Create your views here.
@api_view(['POST'])
def createPost(request):
    data = request.data
    serializer = PostCreateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    
@api_view(['GET'])
def allPosts(request):
    data = PostModel.objects.all()
    serializer = PostViewSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postByUser(request,user_id):
    data = PostModel.objects.filter(uploadedBy=user_id)
    serializer = PostViewSerializer(data, many=True)
    return Response(serializer.data)