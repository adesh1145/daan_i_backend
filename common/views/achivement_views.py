from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from common.models.order_model import OrderModel
from ngo.models.ngo_user_model import NGODetailModel
from donar.models.user_model import UserDetailModel
from daan_i_backend.utils.response_model import responseModel


class AcheiveView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        orderCount = len(OrderModel.objects.all())
        ngoCount = len(NGODetailModel.objects.all())
        donarCount = len(UserDetailModel.objects.all())

        data = [
            {"donationCount": orderCount, "text": "Total Donation"},
            {"ngoCount": ngoCount, "text": "Total NGO"},
            {"donarCount": donarCount, "text": "Total Donar"},
        ]

        return responseModel(status=True, data=data)
