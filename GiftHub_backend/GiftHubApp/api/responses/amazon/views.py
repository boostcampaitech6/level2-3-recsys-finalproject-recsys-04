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

class AmazonPridictionItems(APIView):
    @swagger_auto_schema(
        operation_description="최종 선물 추천",
        tags=['아마존 데이터 추천'],
        responses={200: prediction_items_output_schema(), 400: "Bad Request"}
    )
    def get(self, request, user_id):
        # get user category_1 and price_type
        qs = UserProductInteraction.objects.filter(user_id=user_id)
        serializer = UserProductInteractionSerializer(qs, many=True)
        
        list_product_id = []
        for dict in serializer.data:
            list_product_id.append(dict["product"])
        
        # pridiction items (CF)
        list_predict = bert4rec_predict(list_product_id)
        
        # predict_list select in
        qs = AmazonProduct.objects.filter(product_id__in=list_predict)
        serializer = AmazonProductSerializer(qs, many=True)
        
        return Response(serializer.data)