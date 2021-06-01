from rest_framework.generics import ListAPIView

from .serializers import DiodSerializer, ModelTxtSerializer
from ..models import Diod, ModelTxt


class DiodListAPIView(ListAPIView):

    serializer_class = DiodSerializer
    queryset = Diod.objects.all()

class ModelTxtListAPIView(ListAPIView):

    serializer_class = ModelTxtSerializer
    queryset = ModelTxt.objects.all()
