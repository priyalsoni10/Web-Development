from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer, BookReadSerializer
from .models import BookModel

# Create your views here.
# @api_view(['GET'])
# def getBook(request):
#     bookData = BookModel.objects.all()
#     serializer = BookReadSerializer(bookData , many = True)
#     return Response({"books":serializer.data})
#     # return Response(serializer.data)

# @api_view(['POST'])
# def addBook(request):
#     # data = request.data
#     serializerData = BookSerializer(data = request.data)
#     if serializerData.is_valid():
#         serializerData.save()
#     return Response({"message":"Book Data Added successfully!"})


@api_view(['GET'])
def getBook(request):
    bookData = BookModel.objects.all()
    serializer = BookReadSerializer(bookData, many=True)
    return Response({"books": serializer.data})


@api_view(['GET', 'POST'])   # 👈 sirf POST se GET+POST
def addBook(request):

    if request.method == 'GET':   # 👈 sirf browser ke liye
        return Response({
            "message": "Use POST method to add book"
        })

    serializerData = BookSerializer(data=request.data)
    if serializerData.is_valid():
        serializerData.save()
        return Response({"message": "Book Data Added successfully!"})

    return Response(serializerData.errors, status=400)
