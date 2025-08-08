from django.shortcuts import render, HttpResponse
from .models import Item
from django.http import JsonResponse
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# def item_list(request):
#     items = Item.objects.all()
    
#     ls = []
#     for item in items:
#         ls.append({
#             "name": item.name,
#             "price": item.price,
#             "description": item.description
#         })
    
#     return JsonResponse({"menu_items": ls}, safe=False)

# Serialization = Changing data types into other data types

@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)