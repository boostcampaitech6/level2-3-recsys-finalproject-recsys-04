from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from GiftHubApp.database.models import *
from GiftHubApp.database.serializers import *
from GiftHubApp.open_api_params import *
from GiftHubApp.database.sql_executor import *
from GiftHubApp.api.requests.model_request import *

class AmazonItemsSelect(APIView):
    @swagger_auto_schema(
        operation_description="아마존 아이템 선택",
        tags=['아마존 데이터 추천'],
        responses={200: prediction_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request):
        qs = AmazonProduct.objects.all()
        serializer = AmazonProductSerializer(qs, many=True)
        
        df_product = pd.DataFrame.from_dict(serializer.data, orient="columns")
        df_product = df_product.sample(27)
        
        str_js = df_product.to_json(force_ascii=False, orient="records", indent=4)
        js = json.loads(str_js)
        
        return Response(js)

class AmazonUserInteraction(APIView):
    @swagger_auto_schema(
        operation_description="아마존 유저 인터렉션 데이터 생성",
        tags=['유저 데이터 생성'],
        request_body=create_user_product_interaction_input_schema(),
        responses={200: "HTTP 200 OK", 400: "Bad Request"}
    )
    def post(self, request):
        data = {}
        data['user'] = request.data['user_id']
        data['product'] = request.data['product_id']
        serializer = AmazonUserProductInteractionSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        
        return Response(status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
    operation_description="아마존 유저 인터렉션 데이터 삭제",
    tags=['유저 데이터 삭제'],
    request_body=delete_user_product_interaction_input_schema(),
    responses={200: "HTTP 200 OK", 400: "Bad Request"}
    )
    def delete(self, request):
        user_id = request.data['user_id']
        product_id = request.data['product_id']
        queryset = AmazonUserProductInteraction.objects.filter(Q(user_id=user_id) & Q(product_id=product_id))
        queryset.delete()
        return Response(status=status.HTTP_200_OK)


class AmazonPridictionItems_bert4rec(APIView):
    @swagger_auto_schema(
        operation_description="최종 선물 추천 (BERT4Rec)",
        tags=['아마존 데이터 추천'],
        responses={200: prediction_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request, user_id):
        qs = AmazonUserProductInteraction.objects.filter(user=user_id)
        serializer = AmazonUserProductInteractionSerializer(qs, many=True)
        
        list_product_id = []
        for dict in serializer.data:
            list_product_id.append(dict["product"])
        
        # pridiction items (CF)
        list_predict = predict_bert4rec(list_product_id)
        
        # predict_list select in
        qs = AmazonProduct.objects.filter(product_id__in=list_predict)
        serializer = AmazonProductSerializer(qs, many=True)
        
        return Response(serializer.data)
    
class AmazonPridictionItems_ease(APIView):
    @swagger_auto_schema(
        operation_description="최종 선물 추천 (EASE)",
        tags=['아마존 데이터 추천'],
        responses={200: prediction_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request, user_id):
        qs = AmazonUserProductInteraction.objects.filter(user=user_id)
        serializer = AmazonUserProductInteractionSerializer(qs, many=True)
        
        df_user_interaction = pd.DataFrame.from_dict(serializer.data, orient="columns")
        
        # pridiction items (CF)
        list_predict = predict_ease(df_user_interaction)
        
        # predict_list select in
        qs = AmazonProduct.objects.filter(product_id__in=list_predict)
        serializer = AmazonProductSerializer(qs, many=True)
        
        return Response(serializer.data)
    
class AmazonPridictionItems_lightgcn(APIView):
    @swagger_auto_schema(
        operation_description="최종 선물 추천 (lightgcn)",
        tags=['아마존 데이터 추천'],
        responses={200: prediction_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request, user_id):
        qs = AmazonUserProductInteraction.objects.filter(user=user_id)
        serializer = AmazonUserProductInteractionSerializer(qs, many=True)
        
        list_product_id = []
        for dict in serializer.data:
            list_product_id.append(dict["product"])
        
        # pridiction items (CF)
        list_predict = predict_lightgcn(list_product_id)
        
        # predict_list select in
        qs = AmazonProduct.objects.filter(product_id__in=list_predict)
        serializer = AmazonProductSerializer(qs, many=True)
        
        return Response(serializer.data)
    
class AmazonUserLike(APIView):
    @swagger_auto_schema(
        operation_description="아마존 유저 좋아요 데이터 생성",
        tags=['유저 데이터 생성'],
        request_body=create_user_product_like_input_schema(),
        responses={200: "HTTP 200 OK", 400: "Bad Request"}
    )
    def post(self, request):
        data = {}
        data['user'] = request.data['user_id']
        data['product'] = request.data['product_id']
        serializer = AmazonUserProductLikeSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        
        return Response(status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_description="아마존 유저 좋아요 데이터 삭제",
        tags=['유저 데이터 삭제'],
        request_body=delete_user_product_like_input_schema(),
        responses={200: "HTTP 200 OK", 400: "Bad Request"}
    )
    def delete(self, request):
        user_id = request.data['user_id']
        product_id = request.data['product_id']
        queryset = AmazonUserProductLike.objects.filter(Q(user_id=user_id) & Q(product_id=product_id))
        queryset.delete()
        return Response(status=status.HTTP_200_OK)