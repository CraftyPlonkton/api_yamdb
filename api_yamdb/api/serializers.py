from rest_framework import serializers
from .models import Titles, Generes, Categories


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = "__all__"

class GenereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generes
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
