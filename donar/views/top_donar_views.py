# views.py
from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from ..models.user_model import UserDetailModel
from ..serializers.to_donar_serializer import TopDonorSerializer
from rest_framework.permissions import AllowAny


class TopDonorsView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TopDonorSerializer

    def get_queryset(self):
        return UserDetailModel.objects.annotate(
            total_donations=Count(
                "order_donar"
            )  # order_donar  => order Table ka donar coloumn
        ).order_by("-total_donations")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
