import uuid
from rest_framework import serializers
from common.models.category_model import CategoryModel
from common.models.order_model import *
from donar.models.address_model import AddressModel
from django.utils.translation import gettext
from ngo.serializers.ngo_detail_serializer import *
from donar.models.user_model import UserDetailModel


class DonateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(write_only=True), write_only=True
    )

    class Meta:
        model = OrderModel
        fields = [
            "order_id",
            "category",
            "weight",
            "description",
            "donar",
            "donar_address",
            "ngo",
            "order_status",
            "created_date",
            "updated_date",
            "images",
        ]
        read_only_fields = ["created_date", "updated_date"]

    def to_representation(self, instance):

        return super().to_representation(instance)

    def validate(self, attrs):

        return super().validate(attrs)

    def create(self, validated_data):
        # Set the default order status to 'ongoing'

        validated_data["order_status"] = orderStatus[0][0]
        validated_data["order_id"] = f"DAANI{uuid.uuid4().hex[:6].upper()}"
        images = validated_data.pop("images")
        order = OrderModel.objects.create(**validated_data)
        for image in images:
            OrderImage.objects.create(order=order, image=image)
        return order


class OrderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderImage
        fields = ["id", "image"]


class DonationHistorySerializer(serializers.ModelSerializer):
    image_urls = OrderImageSerializer(source="images", many=True, read_only=True)

    class Meta:
        model = OrderModel
        fields = [
            "id",
            "order_id",
            "category",
            "weight",
            "description",
            "donar",
            "donar_address",
            "ngo",
            "order_status",
            "created_date",
            "updated_date",
            "image_urls",
        ]

    def to_representation(self, instances):

        return super().to_representation(instances)
