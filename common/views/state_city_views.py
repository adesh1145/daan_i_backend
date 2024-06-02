from rest_framework.generics import *
from rest_framework import status
from daan_i_backend.utils.response_model import responseModel

from ..models.state_city_models import CityModel, StateModel
from ..serializers.state_city_serializer import StateSerializer, CitySerializer
from rest_framework.permissions import AllowAny


class StateView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = StateModel.objects.all()
    serializer_class = StateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return responseModel(serializer.data, statusCode=status.HTTP_200_OK)


class CityView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer

    def list(self, request, *args, **kwargs):
        stateId = request.query_params.get("stateId")
        if stateId:
            queryset = CityModel.objects.filter(state_id=stateId)
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return responseModel(serializer.data, statusCode=status.HTTP_200_OK)
