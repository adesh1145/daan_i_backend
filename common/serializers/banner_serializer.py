from rest_framework import serializers
from ..models.banner_model import BannerModel


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerModel
        fields = fields = ["id", "image"]
