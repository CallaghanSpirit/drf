from rest_framework import serializers
from .models import Goods
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ("name","cats_id")