from rest_framework import serializers
from ..models.state_city_models import CityModel, StateModel


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StateModel
        fields = fields = ["id", "name"]


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = StateModel
        fields = fields = ["id", "name", "state"]
