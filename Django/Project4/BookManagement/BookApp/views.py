from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel
from .serializer import BookSerializer

@api_view(['GET'])
def allBooks(request):
    bookData = BookModel.objects.all()
    data = BookSerializer(bookData , many = True)
    return Response({"books":data.data})

@api_view(['GET'])
def getSpecificBook(request,bookId):
    bookData = BookModel.objects.filter(id= bookId)
    return Response({"bookData":bookData.data})


@api_view(['POST'])
def addBook(request):
    # bookData = BookModel.objects.all()
    data = request.data
    serializerData = BookSerializer(data = request.data)
    if serializerData.is_valid():
        serializerData.save()
    return Response({"message":"Data Added successfully!"})

@api_view(['PUT'])
def updateBook(request,bookId):
    bookData = BookModel.objects.get(id=bookId)
    serializerData = BookSerializer(bookData , data = request.data)
    if serializerData.is_valid():
          serializerData.save()
    return Response({"message":"Data Updated Successfully!"})

@api_view(['DELETE'])
def deleteBook(request,bookId):
    data = BookModel.objects.filter(id = bookId)
    data.delete()
    return Response({"message":"Data Deleted Successfully!"})






# Create your views here.
