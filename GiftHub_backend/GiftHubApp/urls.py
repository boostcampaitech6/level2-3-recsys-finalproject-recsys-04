from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from GiftHubApp.views import hello_rest_api, Temp02ListAPI

urlpatterns = [
    path('hello/', hello_rest_api, name='hello_rest_api'),  # FBV(Function Based View)
    path('temp02/<id>/', Temp02ListAPI.as_view()),          # CBV(Class Based View)
]