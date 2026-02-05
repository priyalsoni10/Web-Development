# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AuthorSerializer
from .models import AuthorModel

# Create your views here.
@api_view(['GET'])
def getAuthorInfo(request):
    authorData = AuthorModel.objects.all()
    serializer = AuthorSerializer(authorData , many = True)
    return Response({"authors":serializer.data})
    # return Response(serializer.data)

@api_view(['POST'])
def createAuthorInfo(request):
    # data = request.data
    serializerData = AuthorSerializer(data = request.data)
    if serializerData.is_valid():
        serializerData.save()
    return Response({"message":"Author Data Added successfully!"})
