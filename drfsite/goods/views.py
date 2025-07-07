from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.decorators import action

# Create your views here.

from .models import Goods,Category
from .serializers import GoodsSerializer

class GoodsViewSet(viewsets.ModelViewSet):
    # queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Goods.objects.all()[:1]
        return Goods.objects.filter(pk=pk)
    @action(methods=['get'], detail=True)
    def categories(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats':cats.name})

# class GoodsAPIList(generics.ListCreateAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

# class GoodsAPIUpdate(generics.UpdateAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

# class GoodsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
