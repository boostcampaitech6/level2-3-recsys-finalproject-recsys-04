from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from GiftHubApp.database.models import *
from GiftHubApp.database.serializers import *
from GiftHubApp.database.sql_executor import *
from GiftHubApp.utils import *
from GiftHubApp.open_api_params import *
from GiftHubApp.api.requests.request import *
from GiftHubApp.api.requests.model_request import *

class CreateUser(APIView):
    @swagger_auto_schema(
        operation_description="유저 데이터 생성",
        tags=['유저 데이터 생성'],
        request_body=create_user_input_schema(),
        responses={200: create_user_output_schema(), 400: "Bad Request"}
    )
    def post(self, request):
        # validate user data
        data = {key: request.data[key] for key in ["age", "sex", "price_type", "personality", "category_1"]}
        
        # get user_id
        try:
            sql_exec = SqlExecutor("gifthub")
            sql = sql_get_user_id()
            df = sql_exec.get_sql_to_df(sql)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # insert into user
        data["user_id"] = int(df["user_id"][0])
        serializer_user = UserSerializer(data=data)
        if not serializer_user.is_valid():
            return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer_user.save()
        
        return Response(serializer_user.data)
    
class MatchedItems(APIView):
    @swagger_auto_schema(
        operation_description="마음에 드는 상품을 선택해주세요. (1)",
        tags=['유저 데이터 불러오기'],
        responses={200: matched_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request, user_id):
        # get user category_1 and price_type
        qs = User.objects.filter(user_id=user_id)
        serializer = UserSerializer(qs, many=True)
        
        # get one filtered_item
        try:
            sql_exec = SqlExecutor("gifthub")
            sql_params = {
                "data_1":serializer.data[0]["category_1"],
                "data_2":serializer.data[0]["price_type"]
            }
            sql = sql_get_filtered_item(**sql_params)
            df = sql_exec.get_sql_to_df(sql)
            product_id = df["product_id"][0]
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # lgbm similarlity
        predictions = predict_lgbm(product_id)
        str_js = predictions.to_json(force_ascii=False, orient="records", indent=4)
        js = json.loads(str_js)
        
        return Response(js)

class PridictionItems(APIView):
    @swagger_auto_schema(
        operation_description="최종 선물 추천",
        tags=['유저 데이터 불러오기'],
        responses={200: prediction_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request, user_id):
        # get user category_1 and price_type
        qs = User.objects.filter(user_id=user_id)
        serializer = UserSerializer(qs, many=True)
        
        # pridiction items (CBF)
        
        # pridiction items (CBF)
        
        
        # popular items
        # get user category_1 and price_type
        qs = User.objects.filter(user_id=user_id)
        serializer = UserSerializer(qs, many=True)
        try:
            sql_exec = SqlExecutor("gifthub")
            sql_params = {
                "data_1":user_id,
                "data_2":serializer.data[0]["price_type"],
            }
            sql = sql_get_popular_items_top10(**sql_params)
            js = sql_exec.get_sql_to_json(sql)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(js)

class UserInteraction(APIView):
    @swagger_auto_schema(
        operation_description="유저 인터렉션 데이터 생성",
        tags=['유저 데이터 생성'],
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
    
    @swagger_auto_schema(
        operation_description="유저 인터렉션 데이터 삭제",
        tags=['유저 데이터 삭제'],
        request_body=delete_user_product_interaction_input_schema(),
        responses={200: "HTTP 200 OK", 400: "Bad Request"}
    )
    def delete(self, request):
        user_id = request.data['user_id']
        product_id = request.data['product_id']
        queryset = UserProductInteraction.objects.filter(Q(user_id=user_id) & Q(product_id=product_id))
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
    
class UserLike(APIView):
    @swagger_auto_schema(
        operation_description="유저 좋아요 데이터 생성",
        tags=['유저 데이터 생성'],
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
    
    @swagger_auto_schema(
        operation_description="유저 좋아요 데이터 삭제",
        tags=['유저 데이터 삭제'],
        request_body=delete_user_product_like_input_schema(),
        responses={200: "HTTP 200 OK", 400: "Bad Request"}
    )
    def delete(self, request):
        user_id = request.data['user_id']
        product_id = request.data['product_id']
        queryset = UserProductLike.objects.filter(Q(user_id=user_id) & Q(product_id=product_id))
        queryset.delete()
        return Response(status=status.HTTP_200_OK)