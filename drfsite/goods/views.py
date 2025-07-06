from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework import viewsets

# Create your views here.

from .models import Goods
from .serializers import GoodsSerializer

class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

# class GoodsAPIList(generics.ListCreateAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

# class GoodsAPIUpdate(generics.UpdateAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

# class GoodsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
