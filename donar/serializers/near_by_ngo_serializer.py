from rest_framework import serializers
from common.models.category_model import CategoryModel
from donar.models.address_model import AddressModel
from django.utils.translation import gettext
from ngo.serializers.ngo_detail_serializer import *


class NearByNgoSerializer(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())
    address = serializers.PrimaryKeyRelatedField(queryset=AddressModel.objects.all())

    def validate_address(self, data):
        if (AddressModel.objects.filter(id=data.id, user=self.context)).exists():
            return data
        serializers.ValidationError(gettext("addressNotFound"))

    def to_representation(self, instance):
        step1 = NgoDetailStep1Serializer(
            instance=instance,
        ).data
        step2 = NgoDetailStep2Serializer(
            instance=instance,
        ).data

        step3 = NgoDetailStep3Serializer(instance=instance).data
        step1.update(step2)
        step1.update(step3)
        return step1
