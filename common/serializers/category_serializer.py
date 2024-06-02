from rest_framework import serializers
from ..models.category_model import CategoryModel


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ["id", "category_name", "img"]
