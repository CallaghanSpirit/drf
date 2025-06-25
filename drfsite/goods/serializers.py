from rest_framework import serializers
from .models import Goods
from  rest_framework.parsers import JSONParser
from  rest_framework.renderers import JSONRenderer
import io
class GoodsModel:
    def __init__(self, name):
        self.name = name


    
        
class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    cats_id = serializers.IntegerField()
    def create(self, validated_data):
        return Goods.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.cats_id = validated_data.get("cats_id", instance.cats_id)
        instance.save()
        return instance
    def delete(self, instance):
        instance.delete()
        return instance


# def encode():
#     model = GoodsModel(name="MyName")
#     model_sr = GoodsSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json =  JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"name":"MyName"}')
#     data = JSONParser().parse(stream)
#     serializer = GoodsSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)