from common.models.order_model import *
from daan_i_backend.utils.response_model import responseModel
from ngo.serializers.my_donation_serializer import MyDonationSerializer
from ngo.views.custom_base_auth_apiview import NGOBaseAuthAPIView
from rest_framework import status


class MyDonationView(NGOBaseAuthAPIView):
    def get(self, request, *args, **kwargs):

        order_id = kwargs.get("id")

        order_status = request.query_params.get("donationStatus")

        if order_id is not None:
            orders = OrderModel.objects.filter(ngo=request.user, id=order_id)
            if orders.exists():

                return responseModel(
                    status=True,
                    data={"donation": MyDonationSerializer(orders, many=True).data},
                )
            return responseModel(
                status=False,
                msg="Invalid order id provided.",
            )

        elif order_status and order_status in dict(orderStatus):

            orders = OrderModel.objects.filter(
                ngo=request.user, order_status=order_status
            )
            return responseModel(
                status=True,
                data={"donation": MyDonationSerializer(orders, many=True).data},
            )
        elif order_status:
            return responseModel(
                status=False,
                msg="Invalid order status provided.",
                statusCode=status.HTTP_400_BAD_REQUEST,
            )
        else:
            orders = OrderModel.objects.filter(ngo=request.user)
            return responseModel(
                status=True,
                data={"donation": MyDonationSerializer(orders, many=True).data},
            )
