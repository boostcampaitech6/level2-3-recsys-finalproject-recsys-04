from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# from .api.responses.test.views import *
from .api.responses.user.views import CreateUser, MatchedItems, PridictionItems, UserInteraction, UserLike
from .api.responses.amazon.views import AmazonItemsSelect, AmazonPridictionItems_bert4rec, AmazonPridictionItems_ease

urlpatterns = [
    path('user/', CreateUser.as_view()),
    path('user/matched-items/<user_id>/', MatchedItems.as_view()),
    path('user/items-prediction/<user_id>/', PridictionItems.as_view()),
    path('user/interaction/', UserInteraction.as_view()),
    path('user/like/', UserLike.as_view()),
    path('amazon/items-select/', AmazonItemsSelect.as_view()),
    path('amazon/items-prediction/bert4rec/<user_id>/', AmazonPridictionItems_bert4rec.as_view()),
    path('amazon/items-prediction/ease/<user_id>/', AmazonPridictionItems_ease.as_view())
]

urlpatterns += [
    # path('hello/', hello_rest_api, name='hello_rest_api'),  # FBV(Function Based View)
    # path('temp02/<id>/', Temp02ListAPI.as_view()),          # CBV(Class Based View)
    
]