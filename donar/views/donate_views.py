from common.models.order_model import *
from daan_i_backend.utils.response_model import errorMsg
from donar.serializers.donate_serializer import (
    DonateSerializer,
    DonationHistorySerializer,
)
from donar.views.custom_base_auth_apiview import DonarBaseAuthAPIView
from ..common_imports import *


class DonateView(DonarBaseAuthAPIView):

    def post(self, request, *args, **kwargs):
        if not request.content_type.startswith("multipart/form-data"):
            return responseModel(
                status=False,
                msg=errorMsg("Multipart/form-data content type required."),
                data="Multipart/form-data content type required.",
                statusCode=status.HTTP_400_BAD_REQUEST,
            )

        # request.data["donar"] = request.user
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
        order_id = kwargs.get("id")
        order_status = request.query_params.get("donationStatus")
        if order_id is not None:
            orders = OrderModel.objects.filter(donar=request.user, id=order_id)
            if orders.exists():
                return responseModel(
                    status=True,
                    data={
                        "donation": DonationHistorySerializer(orders, many=True).data
                    },
                )
            return responseModel(
                status=False,
                msg="Invalid order id provided.",
            )

        elif order_status and order_status in dict(orderStatus):

            orders = OrderModel.objects.filter(
                donar=request.user, order_status=order_status
            )
            return responseModel(
                status=True,
                data={"donation": DonationHistorySerializer(orders, many=True).data},
            )
        elif order_status:
            return responseModel(
                status=False,
                msg="Invalid order status provided.",
                statusCode=status.HTTP_400_BAD_REQUEST,
            )
        else:
            orders = OrderModel.objects.filter(donar=request.user)
            return responseModel(
                status=True,
                data={"donation": DonationHistorySerializer(orders, many=True).data},
            )
