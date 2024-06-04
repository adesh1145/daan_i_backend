# views.py
from django.db.models import Count
from rest_framework import generics
from ..models.user_model import UserDetailModel
from ..serializers.to_donar_serializer import TopDonorSerializer
from rest_framework.permissions import AllowAny
from ..common_imports import *


class TopDonorsView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TopDonorSerializer

    def get_queryset(self):
        return (
            UserDetailModel.objects.annotate(total_donations=Count("order_donar"))
            .filter(total_donations__gt=0)
            .order_by("-total_donations")[:5]
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return responseModel(status=True, data=serializer.data)
