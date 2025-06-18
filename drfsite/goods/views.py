
from rest_framework import generics
# Create your views here.

from .models import Goods
from .serializers import GoodsSerializer

class GoodsAPIView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
