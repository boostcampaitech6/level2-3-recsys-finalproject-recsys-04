from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from GiftHubApp.models import Temp02
from GiftHubApp.serializers import Temp02Serializer

@api_view(['GET'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data, status=status.HTTP_200_OK)

class Temp02ListAPI(APIView):
    def get(self, request, id):
        queryset = Temp02.objects.filter(id=id)
        serializer = Temp02Serializer(queryset, many=True)
        print(type(serializer.data))
        return Response(serializer.data)
