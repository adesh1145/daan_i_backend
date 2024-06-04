from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from common.models.order_model import *
from ngo.models.ngo_user_model import NGODetailModel
from donar.models.user_model import UserDetailModel
from daan_i_backend.utils.response_model import responseModel
from django.db.models import Count, Q


class AcheiveView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        orderCount = OrderModel.objects.filter(
            Q(order_status=orderStatus[2][0])
        ).aggregate(total_count=Count("id"))["total_count"]
        pending_count = OrderModel.objects.filter(
            Q(order_status=orderStatus[0][0])
            | Q(order_status=orderStatus[1][0])
            | Q(order_status=orderStatus[3][0])
            | Q(order_status=orderStatus[4][0])
        ).aggregate(total_count=Count("id"))["total_count"]
        ngoCount = len(NGODetailModel.objects.all())
        donarCount = len(UserDetailModel.objects.all())

        data = [
            {"count": orderCount, "text": "Total Donation"},
            {"count": pending_count, "text": "Pending Donation"},
            {"count": donarCount, "text": "Total Donar"},
            {"count": ngoCount, "text": "Total NGO"},
        ]

        return responseModel(status=True, data=data)
