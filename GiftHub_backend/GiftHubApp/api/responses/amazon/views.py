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
from GiftHubApp.models.model_serveing import *

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

class AmazonPridictionItems_bert4rec(APIView):
    @swagger_auto_schema(
        operation_description="최종 선물 추천 (BERT4Rec)",
        tags=['아마존 데이터 추천'],
        responses={200: prediction_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request, user_id):
        qs = AmazonUserInteraction.objects.filter(user_id=user_id)
        serializer = AmazonUserInteractionSerializer(qs, many=True)
        
        list_product_id = []
        for dict in serializer.data:
            list_product_id.append(dict["product"])
        
        # pridiction items (CF)
        list_predict = bert4rec_predict(list_product_id)
        
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
        qs = AmazonUserInteraction.objects.filter(user_id=user_id)
        serializer = AmazonUserInteractionSerializer(qs, many=True)
        
        df_user_interaction = pd.DataFrame.from_dict(serializer.data, orient="columns")
        
        # pridiction items (CF)
        list_predict = ease_predict(df_user_interaction)
        
        # predict_list select in
        qs = AmazonProduct.objects.filter(product_id__in=list_predict)
        serializer = AmazonProductSerializer(qs, many=True)
        
        return Response(serializer.data)