# Create your views here.
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
menu = []
orders = []  
@api_view(['Get'])
def getMenu(request):
    return Response({"Food Item":menu})
@api_view(['POST'])
def createItem(request):
      menu.append(request.data)
      return Response({
           "message":"created Successfully! "
      })

@api_view(['GET'])
def dishById(request,id):
    data = ""
    for i in menu:
        if i["id"]== id:
           data = i
           break
    if data == "" :
        data = "Not Found" 
    return Response({
        "message" : data
    }) 

@api_view(['GET']) 
def  dishByName(request):
    name = request.query_params.get("name")
    data = []
    for i in menu:
        if i.get("name") == name:
            data.append(i)
    if not data:
        return Response({
            "message":"Not Found"
        })    
    return Response({
        "message" : data
    })  

@api_view(['PUT']) 
def updateItem(request,id):
    for i in menu:
        if i["id"] == id:
            i["name"] = request.data["name"]
            i["price"] = request.data["price"]
            i["available"] = request.data["available"]
            return Response({
                "message": "Updated Successfully",
                "data": i
            })  
    return Response({
        "message": "Item Not Found"            
    })    

@api_view(['DELETE']) 
def deleteItem(request,id):
    for i in menu:
        if i["id"] == id:
            menu.remove(i)
            return Response({
                "message": "Deleted Successfully",
                "data": i
            })  
    return Response({
        "message": "Item Not Found"            
    })   

@api_view(['POST'])
def makeOrder(request):
    order_items = []
    total = 0

    # loop through each item in request
    for item in request.data["items"]:
        for m in menu:
            if m["id"] == item["id"] and m["available"]:
                price = m["price"] * item["quantity"]
                total += price
                order_items.append({
                    "id": m["id"],
                    "name": m["name"],
                    "quantity": item["quantity"],
                    "price": price
                })

    order = {
        "orderId": request.data["orderId"],
        "customerName": request.data["customerName"],  # 👈 यही missing था
        "items": order_items,
        "total": total
    }

    orders.append(order)

    return Response({
        "message": "Order Created Successfully",
        "order": order
    })


@api_view(['PUT'])
def updateOrder(request, id):
    for order in orders:
        if order["orderId"] == id:
            order_items = []
            total = 0

            for item in request.data["items"]:
                for m in menu:
                    if m["id"] == item["id"] and m["available"]:
                        price = m["price"] * item["quantity"]
                        total += price
                        order_items.append({
                            "id": m["id"],
                            "name": m["name"],
                            "quantity": item["quantity"],
                            "price": price
                        })

            order["items"] = order_items
            order["total"] = total

            return Response({
                "message": "Order Updated Successfully",
                "order": order
            })

    return Response({
        "message": "Order Not Found"
    })

@api_view(['GET'])
def getBill(request, id):
    for order in orders:
        if order["orderId"] == id:
            bill_items = []
            total = 0

            for item in order["items"]:
                for m in menu:
                    if m["id"] == item["id"]:
                        item_total = m["price"] * item["quantity"]
                        total += item_total

                        bill_items.append({
                            "itemName": m["name"],
                            "price": m["price"],
                            "quantity": item["quantity"],
                            "itemTotal": item_total
                        })

            return Response({
                "orderId": order["orderId"],
                "customerName": order["customerName"],
                "items": bill_items,
                "totalAmount": total
            })

    return Response({"message": "Order not found"})

