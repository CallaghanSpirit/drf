from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.forms.models import model_to_dict

# Create your views here.

from .models import Goods
from .serializers import GoodsSerializer

class GoodsAPIView(APIView):
    def get(self, request):
        lst = Goods.objects.all().values()
        return Response({"goods": list(lst)})
    def post(self, request):
        post_new = Goods.objects.create(name=request.data['name'],
                                         cats_id=request.data['cats_id'])
        return Response({"post":model_to_dict(post_new)})


# class GoodsAPIView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
