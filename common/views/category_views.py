from rest_framework.generics import *
from rest_framework import status
from daan_i_backend.utils.response_model import responseModel

from ..models.category_model import CategoryModel
from ..serializers.category_serializer import CategorySerializer


class CategoryView(ListAPIView):

    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return responseModel(serializer.data, statusCode=status.HTTP_200_OK)
