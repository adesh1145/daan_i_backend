from daan_i_backend.utils.response_model import errorMsg
from donar.views.custom_base_auth_apiview import DonarBaseAuthAPIView
from ..common_imports import *
from ..serializers.near_by_ngo_serializer import NearByNgoSerializer
from ngo.models.ngo_user_model import NGODetailModel
from ngo.serializers.ngo_detail_serializer import (
    NgoDetailStep1Serializer,
    NgoDetailStep3Serializer,
)
from ..models.address_model import AddressModel


class NearByNgoView(DonarBaseAuthAPIView):

    def get(self, request, *args, **kwargs):
        request.user
        serializer = NearByNgoSerializer(data=request.data, context=request.user)
        if serializer.is_valid():
            ngo = NGODetailModel.objects.filter(
                city=AddressModel.objects.get(
                    id=serializer.validated_data["address"].id
                ).city
            )
            serializedNgo = NearByNgoSerializer(ngo, many=True)
            return responseModel(status=True, data={"ngo": serializedNgo.data})
        return responseModel(
            status=False,
            msg=errorMsg(serializer.errors),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )
