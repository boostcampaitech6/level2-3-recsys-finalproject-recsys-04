from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from GiftHubApp.models import *
from GiftHubApp.utils import *
from GiftHubApp.open_api_params import *
from .serializers import *

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
        
        try:
            js = db_get_matched_items("gifthub", category_1, price_type)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(js)
    
class CreateUserProductInteraction(APIView):
    @swagger_auto_schema(
        operation_description="마음에 드는 상품의 유저 Interaction",
        request_body=create_user_product_interaction_input_schema(),
        responses={200: "HTTP 200 OK", 400: "Bad Request"}
    )
    def post(self, request):
        data = {}
        data['user'] = request.data['user_id']
        data['product'] = request.data['product_id']
        serializer = UserProductInteractionSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        
        return Response(status=status.HTTP_200_OK)
    
class CreateUserProductLike(APIView):
    @swagger_auto_schema(
        operation_description="유저 좋아요 피드백",
        request_body=create_user_product_like_input_schema(),
        responses={200: "HTTP 200 OK", 400: "Bad Request"}
    )
    def post(self, request):
        data = {}
        data['user'] = request.data['user_id']
        data['product'] = request.data['product_id']
        serializer = UserProductLikeSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        
        return Response(status=status.HTTP_200_OK)