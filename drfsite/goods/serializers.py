from rest_framework import serializers
from .models import Goods
from  rest_framework.parsers import JSONParser
from  rest_framework.renderers import JSONRenderer
import io

    
        
class GoodsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Goods
        fields = ("name","cats",'user')

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