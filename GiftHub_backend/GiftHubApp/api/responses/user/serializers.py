from rest_framework import serializers

from GiftHubApp.models import *

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