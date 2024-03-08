from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.responses.test.views import *
from .api.responses.user.views import *

urlpatterns = [
    path('user/', CreateUser.as_view()),
    path('user/matched-items/<user_id>/', MatchedItems.as_view()),
    path('user/interaction/', CreateUserProductInteraction.as_view()),
    path('user/like/', CreateUserProductLike.as_view()),
]

urlpatterns += [
    path('hello/', hello_rest_api, name='hello_rest_api'),  # FBV(Function Based View)
    path('temp02/<id>/', Temp02ListAPI.as_view()),          # CBV(Class Based View)
]