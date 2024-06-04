from rest_framework import serializers

from common.serializers.state_city_serializer import CitySerializer, StateSerializer
from ..models.ngo_user_model import NGODetailModel
from donar.models.user_model import UserDetailModel

# Create your models here.
from django.utils.translation import gettext as _
from common.models.state_city_models import CityModel, StateModel
from common.models.category_model import CategoryModel
from common.serializers.category_serializer import CategorySerializer


class NgoDetailStep1Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ngo_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    mobile = serializers.CharField(max_length=10)
    password = serializers.CharField(write_only=True, max_length=100)
    t_and_c_status = serializers.BooleanField(write_only=True, default=False)

    def __str__(self):
        return self.ngo_name

    def validate_email(self, value):
        """
        Check if the email is unique.
        """
        if NGODetailModel.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("EmailisAlreadyExists"))
        elif UserDetailModel.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("EmailisAlreadyExistsInDonar"))
        return value

    def validate_t_and_c_status(self, data):
        if data == True:
            return data
        raise serializers.ValidationError(_("term&ConditionssholudbeTrue"))

    def create(self, validated_data):
        """
        Create and return a new `NGO` instance.
        """
        return NGODetailModel.objects.create(**validated_data)

    def update(self, instance, validated_data: dict):
        # validated_data.get('name')
        name = validated_data["ngo_name"]
        validated_data.clear()
        validated_data = {"ngo_name": name}
        setattr(instance, "ngo_name", name)
        return instance.save()


class NgoDetailStep2Serializer(serializers.Serializer):

    ngo_image = serializers.ImageField()
    reg_certificate_image = serializers.ImageField()
    pan_card_image = serializers.ImageField()
    ngo_owner_ame = serializers.CharField(
        max_length=255,
    )
    reg_certificate_no = serializers.CharField(max_length=255)
    pan_no = serializers.CharField(
        max_length=255,
    )
    gst_no = serializers.CharField(
        max_length=255,
    )
    accept_category = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )
    accept_category_details = serializers.SerializerMethodField()

    def get_accept_category_details(self, obj):

        categories = obj.accept_category.all()

        return CategorySerializer(categories, many=True).data

    def validate(self, attrs):
        # print(attrs)
        return super().validate(attrs)

    def validate_id(self, data):
        if not NGODetailModel.objects.filter(id=data).exists():
            raise serializers.ValidationError(_("UserDoesNotExist"))
        elif not NGODetailModel.objects.get(id=data).is_verified == True:
            raise serializers.ValidationError(_("yourAccountIsNotVerify"))
        return data

    def validate_accept_category(self, data):
        # for value in data:
        if CategoryModel.objects.filter(id__in=data).exists():
            return data
        return serializers.ValidationError(_("categotyIdDoesNotExist"))

    def update(self, instance: NGODetailModel, validated_data: dict):
        categoryList = validated_data.pop("accept_category", [])

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.registration_step = 2
        instance.accept_category.set(categoryList)
        instance.save()
        return instance


class NgoDetailStep3Serializer(serializers.Serializer):

    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    address = serializers.CharField(
        max_length=255,
    )
    landmark = serializers.CharField(
        max_length=255,
    )
    pincode = serializers.IntegerField()
    state = serializers.PrimaryKeyRelatedField(queryset=StateModel.objects.all())
    state_detail = serializers.SerializerMethodField()
    city = serializers.PrimaryKeyRelatedField(queryset=CityModel.objects.all())
    city_detail = serializers.SerializerMethodField()

    def validate(self, attrs):
        # print(attrs)
        return super().validate(attrs)

    def validate_id(self, data):
        if not NGODetailModel.objects.filter(id=data).exists():
            raise serializers.ValidationError(_("UserDoesNotExist"))
        elif not NGODetailModel.objects.get(id=data).is_verified == True:
            raise serializers.ValidationError(_("yourAccountIsNotVerify"))
        return data

    def get_city_detail(self, obj):

        cities = CitySerializer(
            obj.city,
        ).data
        cities.pop("state")
        return cities

    def get_state_detail(self, obj):

        states = obj.state
        return StateSerializer(
            states,
        ).data

    def validate_city(self, value):

        if CityModel.objects.filter(
            id=value.id, state=self.initial_data.get("state")
        ).exists():
            return value
        raise serializers.ValidationError(_("CityIdNotExistInThisState"))

    def update(self, instance: NGODetailModel, validated_data: dict):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.registration_step = 3
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
        if NGODetailModel.objects.filter(email=value).exists():

            return value
        else:
            raise serializers.ValidationError(_("ThisEmailisNotExists"))
