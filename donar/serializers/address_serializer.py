from email.policy import default
from rest_framework import serializers

from common.models.state_city_models import CityModel, StateModel
from common.serializers.state_city_serializer import CitySerializer, StateSerializer
from donar.models.address_model import AddressModel
from donar.models.user_model import UserDetailModel
from django.utils.translation import gettext


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    address = serializers.CharField(max_length=255)
    landmark = serializers.CharField(max_length=255)
    pincode = serializers.IntegerField()
    state = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=StateModel.objects.all())
    state_detail = serializers.SerializerMethodField()

    city = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=CityModel.objects.all())
    city_detail = serializers.SerializerMethodField()
    is_default = serializers.BooleanField(default=False)
    # user = serializers.PrimaryKeyRelatedField(
    #     queryset=UserDetailModel.objects.all())

    def __init__(self, *args, **kwargs):
        super(AddressSerializer, self).__init__(*args, **kwargs)
        request = self.context
        # if request:
        #     if request.method in ['PUT', 'PATCH', 'DELETE']:
        #         print("Yess")
        #         self.fields['id'].required = True
        #     elif request.method == 'POST':
        #         self.fields['id'].required = False

    def validate_city(self, value):

        if CityModel.objects.filter(id=value.id, state=self.initial_data.get('state')).exists():
            return value
        raise serializers.ValidationError(gettext("CityIdNotExistInThisState"))

    def get_state_detail(self, obj):
        print(obj.state)
        states = obj.state
        return StateSerializer(states, ).data

    def get_city_detail(self, obj):

        cities = CitySerializer(obj.city, ).data
        cities.pop('state')
        return cities

    def create(self, validated_data):
        user = self.context.user
        if UserDetailModel.objects.filter(id=user.id).exists():
            validated_data['user'] = user
            return AddressModel.objects.create(**validated_data)

        raise serializers.ValidationError(gettext("CityIdNotExistInThisState"))

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get(
            'longitude', instance.longitude)
        instance.address = validated_data.get('address', instance.address)
        instance.landmark = validated_data.get('landmark', instance.landmark)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.state = validated_data.get('state', instance.state)
        checkCity(self, instance.state, validated_data.get('city'))
        instance.city = validated_data.get('city', instance.city)
        instance.is_default = validated_data.get(
            "is_default", instance.is_default)

        return instance.save()


def checkCity(self, state, city):
    if CityModel.objects.filter(id=city.id, state=state).exists():
        return city
