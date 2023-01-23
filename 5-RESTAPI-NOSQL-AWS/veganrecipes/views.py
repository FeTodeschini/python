import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import boto3

@api_view(['GET','POST'])
def recipes(request):
    db = boto3.resource('dynamodb')
    table = db.Table('veganrecipes')

    if request.method == 'GET':
        recipes = table.scan()
        return Response({'recipes': recipes.get('Items')})
    elif request.method == 'POST':
        try:
            table.put_item(Item = request.data)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({'Error':'Failed to insert.'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','PUT', 'DELETE'])
def recipe(request, recipe):
    db = boto3.resource('dynamodb')
    table = db.Table('veganrecipes')
    recipe = table.get_item(Key={
        'recipe': recipe
    })

    if request.method == 'GET':

        if recipe.get('Item') is not None:
            return Response({'recipe': recipe.get('Item')})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        try:
            table.put_item(Item = request.data)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response({'Error':'Failed to update.'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'DELETE':
        table.delete_item(Key={
            'recipe': recipe
        })
        return Response(status=status.HTTP_200_OK)
        
