from rest_framework import serializers
from ..models.user_model import UserDetailModel

# Create your models here.
from django.utils.translation import gettext as _


class UserDetailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    mobile = serializers.CharField(
        max_length=10,
        allow_blank=True,
    )
    password = serializers.CharField(write_only=True, max_length=100)
    # created_date = serializers.DateTimeField(read_only=True)  # Created date as read-only
    # updated_date = serializers.DateTimeField(read_only=True)
    profile_image = serializers.ImageField(required=False)  # Store image URL
    address = serializers.CharField(max_length=255, required=False)

    def __str__(self):
        return self.name

    def validate_email(self, value):
        """
        Check if the email is unique.
        """
        if UserDetailModel.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("EmailisAlreadyExists"))
        return value

    def create(self, validated_data):
        """
        Create and return a new `Donars` instance.
        """
        return UserDetailModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.profile_image = validated_data.get(
            "profile_image", instance.profile_image
        )

        instance.save()

        return instance


class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()

    def validate_otp(self, value):

        if len(str(value)) != 4:
            raise serializers.ValidationError("Value must be a 4-digit number.")
        return value


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        if UserDetailModel.objects.filter(email=value).exists():

            return value
        else:
            raise serializers.ValidationError("This Email is Not Exists")
