from common.models.order_model import OrderModel
from daan_i_backend.utils.response_model import errorMsg
from donar.serializers.donate_serializer import (
    DonateSerializer,
    DonationHistorySerializer,
)
from donar.views.custom_base_auth_apiview import DonarBaseAuthAPIView
from ..common_imports import *
from ngo.models.ngo_user_model import NGODetailModel


class DonateView(DonarBaseAuthAPIView):

    def post(self, request, *args, **kwargs):
        request.data["donar"] = request.user.id
        order_id = kwargs.get("id")

        serializer = DonateSerializer(data=request.data, context=request.user)
        if serializer.is_valid():
            order = serializer.save()
            return responseModel(
                msg=gettext("Donation Request Sent"),
                status=True,
                data={"donation_id": order.id},
            )
        return responseModel(
            status=False,
            msg=errorMsg(serializer.errors),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )


class DonationHistoryView(DonarBaseAuthAPIView):
    def get(self, request, *args, **kwargs):
        request.user.id
        order_id = kwargs.get("id")
        if order_id:
            orders = OrderModel.objects.filter(donar=request.user, id=order_id)

            return responseModel(
                status=True,
                data={"donation": DonationHistorySerializer(orders, many=True).data},
            )
        else:
            orders = OrderModel.objects.filter(donar=request.user)

            return responseModel(
                status=True,
                data={"donation": DonationHistorySerializer(orders, many=True).data},
            )
