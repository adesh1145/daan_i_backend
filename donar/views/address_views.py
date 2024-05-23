from daan_i_backend.utils.response_model import errorMsg
from donar.models.address_model import AddressModel
from donar.views.custom_base_auth_apiview import DonarBaseAuthAPIView
from ..common_imports import *
from ..serializers.address_serializer import AddressSerializer


class AddressView(DonarBaseAuthAPIView):

    def get(self, request, *args, **kwargs):
        addrss = AddressModel.objects.filter(user=request.user)

        return responseModel(
            status=True, data={"address": AddressSerializer(addrss, many=True).data}
        )

    def post(self, request, *args, **kwargs):

        serializer = AddressSerializer(data=request.data, context=request)

        if serializer.is_valid():
            address = serializer.save()
            return responseModel(
                {"message": gettext("addressAdded")}, msg=gettext("addressAdded")
            )
        return responseModel(
            status=False,
            msg=errorMsg(serializer.errors),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, *args, **kwargs):

        serializer = AddressSerializer(data=request.data, context=request, partial=True)

        if serializer.is_valid():
            print(serializer.validated_data["id"])
            address = serializer.update(
                validated_data=serializer.validated_data,
                instance=AddressModel.objects.get(id=serializer.validated_data["id"]),
            )
            return responseModel(
                {"message": gettext("addressUpdated")}, msg=gettext("addressUpdated")
            )
        return responseModel(
            status=False,
            msg=errorMsg(serializer.errors),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, *args, **kwargs):
        address_id = kwargs.get("id")
        print(address_id)
        if address_id:
            if AddressModel.objects.filter(id=address_id).exists():
                address = AddressModel.objects.get(id=address_id)
                address.delete()
                return responseModel(status=True, msg=gettext("addressDeleted"))
            responseModel(
                status=False,
                msg=gettext("thisAddressDoesNotExist"),
                statusCode=status.HTTP_400_BAD_REQUEST,
            )

        return responseModel(
            status=False,
            msg=gettext("thisAddressDoesNotExist"),
            statusCode=status.HTTP_400_BAD_REQUEST,
        )
