from django.shortcuts import render
from app1.models import Product
from app1.serializers import productserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


# LIST VIEW & CREATE VIEW
# function to read(GET) all the data present in our model, in JSON format
# function to add(insert) new recorsd in the our model , in JSON format

@api_view(['GET','POST'])
def productlist(request):
    # code to get(read) all data
    if request.method == 'GET':
        obj = Product.objects.all() # all the data of product model is present in "obj" but in dictionary form
        serializer = productserializer(obj,many = True) # all the data present "obj" is coverted into JSON format & saves into serializer
        return Response(serializer.data) # this will return all data present in serializer

    # code to add(insert) new data
    if request.method == 'POST':
        serializer = productserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



# DETAIL VIEW , UPDATE VIEW , DELETE VIEW
# function to get the data of specific id , into JSON format

@api_view(['GET','PUT','DELETE'])
def productdetail(request,pk):
    try:
        obj = Product.objects.get(id = pk) # only the data of specific id is present in the "obj" in dictionary form
    except Product.DoesNotExist: # if the entered product is not present in the model than this block will handle(except) the error
        return Response(status=status.HTTP_404_NOT_FOUND)

    # code to get the deatils of any specific product by id
    if request.method == 'GET':
        serializer = productserializer(obj) # all the data present "obj" is coverted into JSON format & saves into serializer
        return Response(serializer.data) # this will return all data present in serializer

    # code to update products
    elif request.method == 'PUT':
        serializer = productserializer(obj,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # code to delete product
    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_200_OK)
