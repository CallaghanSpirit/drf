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
        serializer = GoodsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({"post":serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Goods.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = GoodsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            instance = Goods.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        instance.delete()
        return Response({"post": "delete post " + str(pk)})


# class GoodsAPIView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
