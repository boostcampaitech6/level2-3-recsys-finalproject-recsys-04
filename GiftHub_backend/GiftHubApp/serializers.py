from rest_framework import serializers

from GiftHubApp.models import *

class Temp02Serializer(serializers.ModelSerializer) :
    class Meta :
        model = Temp02        # Temp02 모델 사용
        fields = '__all__'    # 모든 필드 포함
        
class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = '__all__'