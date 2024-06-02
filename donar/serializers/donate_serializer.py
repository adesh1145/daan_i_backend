import uuid
from rest_framework import serializers
from common.models.order_model import *
from django.utils.translation import gettext
from donar.serializers.near_by_ngo_serializer import NearByNgoSerializer
from donar.serializers.address_serializer import AddressSerializer
from ngo.serializers.ngo_detail_serializer import *


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
    ngo_detail = NearByNgoSerializer(source="ngo")
    pickup_address = AddressSerializer(source="donar_address")

    class Meta:
        model = OrderModel
        fields = [
            "id",
            "order_id",
            "category",
            "weight",
            "description",
            "pickup_address",
            "ngo",
            "ngo_detail",
            "order_status",
            "created_date",
            "updated_date",
            "image_urls",
        ]

    def to_representation(self, instances):

        return super().to_representation(instances)
