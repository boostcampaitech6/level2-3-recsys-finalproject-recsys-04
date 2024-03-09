from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from GiftHubApp.database.models import *
from GiftHubApp.utils import *
from GiftHubApp.open_api_params import *
from GiftHubApp.database.serializers import *

# @api_view(["GET"])
# @permission_classes([AllowAny])
# def hello_rest_api(request):
#     data = {"message": "Hello, REST API!"}
    
#     return Response(data, status=status.HTTP_200_OK)

# class Temp02ListAPI(APIView):
#     @swagger_auto_schema(
#         operation_description="temp02 조회 테스트"
#     )
#     def get(self, request, id):
#         queryset = Temp02.objects.filter(id=id)
#         serializer = Temp02Serializer(queryset, many=True)
        
#         return Response(serializer.data[0])
