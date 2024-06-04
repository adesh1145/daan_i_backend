# serializers.py
from rest_framework import serializers
from ..models.user_model import UserDetailModel


class TopDonorSerializer(serializers.ModelSerializer):
    total_donations = serializers.IntegerField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserDetailModel
        fields = "__all__"
