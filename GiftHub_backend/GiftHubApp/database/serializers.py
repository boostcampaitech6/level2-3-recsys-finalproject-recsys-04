from rest_framework import serializers

from GiftHubApp.database.models import *

class Temp02Serializer(serializers.ModelSerializer) :
    class Meta :
        model = Temp02        # Temp02 모델 사용
        fields = '__all__'    # 모든 필드 포함

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = '__all__'
        
class UserProductInteractionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserProductInteraction
        fields = '__all__'
        
class UserProductLikeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserProductLike
        fields = '__all__'
        
class FilteredRawdataSerializer(serializers.ModelSerializer) :
    class Meta :
        model = FilteredRawdata
        fields = '__all__'

class AmazonProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = AmazonProduct
        fields = ["product_id", "product_name", "image_url"]

class AmazonUserProductInteractionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = AmazonUserProductInteraction
        fields = '__all__'

class AmazonUserProductLikeSerializer(serializers.ModelSerializer):
    class Meta :
        model = AmazonUserProductLike
        fields = '__all__'
    