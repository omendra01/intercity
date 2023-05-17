from django.db import router
from django.urls import path,include
from demoapp import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('result',views.ResultViews,basename='result')

urlpatterns = [
    
    path('',include(router.urls)),
   
]