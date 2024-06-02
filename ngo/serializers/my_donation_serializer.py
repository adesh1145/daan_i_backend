from rest_framework import serializers

from common.models.order_model import OrderModel
from donar.serializers.address_serializer import AddressSerializer
from donar.serializers.donate_serializer import OrderImageSerializer


class MyDonationSerializer(serializers.ModelSerializer):
    image_urls = OrderImageSerializer(source="images", many=True, read_only=True)

    pickup_address = AddressSerializer(source="donar_address")

    class Meta:
        model = OrderModel
        fields = [
            "id",
            "order_id",
            "category",
            "weight",
            "description",
            "donar",
            "pickup_address",
            "order_status",
            "created_date",
            "updated_date",
            "image_urls",
        ]
