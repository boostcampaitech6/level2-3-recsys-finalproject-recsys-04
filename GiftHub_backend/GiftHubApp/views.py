import json
from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from GiftHubApp.models import *
from GiftHubApp.serializers import *
from GiftHubApp.utils import *
from GiftHubApp.open_api_params import *

@api_view(["GET"])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {"message": "Hello, REST API!"}
    return Response(data, status=status.HTTP_200_OK)

class Temp02ListAPI(APIView):
    @swagger_auto_schema(
        operation_description="temp02 조회 테스트"
    )
    def get(self, request, id):
        queryset = Temp02.objects.filter(id=id)
        serializer = Temp02Serializer(queryset, many=True)
        return Response(serializer.data[0])

class CreateUser(APIView):
    @swagger_auto_schema(
        operation_description="유저 데이터 생성",
        request_body=create_user_input_schema(),
        responses={200: create_user_output_schema(), 400: "Bad Request"}
    )
    def post(self, request):
        # user data valid
        data = {key: request.data[key] for key in ["age", "sex", "price_type", "personality", "category_1"]}
        user_id = db_get_seq("gifthub", User._meta.db_table)
        data["user_id"] = user_id
        serializer_user = UserSerializer(data=data)
        if not serializer_user.is_valid():
            return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer_user.save()
        return Response(serializer_user.data)
    
class MatchedItems(APIView):
    @swagger_auto_schema(
        operation_description="마음에 드는 상품을 선택해주세요. (1)",
        responses={200: matched_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request, user_id):
        qs = User.objects.filter(user_id=user_id)
        serializer = UserSerializer(qs, many=True)
        category_1 = serializer.data[0]["category_1"]
        price_type = serializer.data[0]["price_type"]
        
        js = db_get_matched_items("gifthub", category_1, price_type)
        return Response(js)