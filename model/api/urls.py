from django.urls import path

from .api_views import DiodListAPIView, ModelTxtListAPIView

urlpatterns = [
    path('diod/', DiodListAPIView.as_view(), name='aboutmodels'),
    path('modeltxt/', ModelTxtListAPIView.as_view(), name='modeltxt')
]
