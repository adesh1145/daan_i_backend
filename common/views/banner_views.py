from rest_framework.generics import *
from rest_framework import status
from daan_i_backend.utils.response_model import responseModel

from ..models.banner_model import BannerModel
from ..serializers.banner_serializer import BannerSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny


class BannerView(ListAPIView):

    permission_classes = [AllowAny]
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return responseModel(serializer.data, statusCode=status.HTTP_200_OK)
