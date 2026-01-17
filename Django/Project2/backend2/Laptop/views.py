# Create your views here.
"""
Laptop Inventory:
1.Create New Laptop Data
2.See All Laptops
3.See the laptops by brand  name
4.See one specific laptop
5.Update Laptop Data
6.Delete Laptop Data
Base URL = "https://127.0.0.1:8000/api/Laptop"
API End Points
POST/createLaptop
GET/allLaptops
GET/allLaptops?brand="Dell"
GET/laptop/101
PUT/UpdateLaptop/101
DELETE/delete/101 
// Sample response for one laptop
{
"id" : 101,
"Brand" : "Dell",
"Model" : "XPS 30",
"Price" : 150000,
"Poster" : "Laptop.jpg"
}

"""
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
laptopData = []
@api_view(['GET'])
def getALLLaptop(request):
    return Response({"laptopData":laptopData})

@api_view(['POST'])
def createLaptop(request):
    laptopData.append(request.data)
    return Response({
        "message":"Created Successfully!"
    })
@api_view(['GET'])
def oneLaptop(request,id):
    # print(id)
    data =""
    for l in laptopData:
        if l["id"] == id:
            data = l
            break
    if data == "":
        data = "Not Found"    
    return Response({
        "message" : data
    })

@api_view(['GET'])
# def laptopByBrand(request):
#     brand = request.query_params.get("brand")
#     return Response({
#         "message" : brand
#     })

def laptopByBrand(request):
    brand = request.query_params.get("brand")

    result = []
    for l in laptopData:
        if l.get("Brand") == brand:
            result.append(l)

    if not result:
        return Response({
            "message": "Not Found"
        })

    return Response({
        "count": len(result),
        "data": result
    })

@api_view(['PUT'])
def updateLaptop(request,id):
    for i in laptopData:
        if i["id"] == id:
            i["Brand"] = request.data["Brand"]
            i["Model"] = request.data["Model"]
            i["Price"] = request.data["Price"]
            break
    return Response({
        "message":"Update Successfully!"
    }) 


@api_view(['DELETE']) 
def deleteLaptop(reequest,id):
    for i in laptopData:
        if i["id"] == id:
            laptopData.remove(i)
            break
    return Response({
        "messege" : "Delete Successfully!"
    })      


