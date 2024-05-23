# Create your views here.

from ngo.views.custom_base_auth_apiview import NGOBaseAuthAPIView
from daan_i_backend.utils.response_model import errorMsg, responseModel
from ..common_imports import *
from ..serializers.ngo_detail_serializer import *
from ..models.ngo_user_model import NGODetailModel

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class NGORegistrationStep1View(NGOBaseAuthAPIView):
    except_token_Api_method = ["POST"]

    def get(self, request, *args, **kwargs):

        user = request.user

        if user:
            return responseModel(
                status=True, data=NgoDetailStep1Serializer(instance=user).data
            )
        return responseModel(
            status=False,
            msg=errorMsg("UserDetailNotExist"),
            data="UserDetailNotExist",
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def post(self, request):
        serializer = NgoDetailStep1Serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = generate_otp()
            subject = "Daan-i OTP Verification"
            message = f"Your OTP Is {otp}"
            sendEmail(subject, message, serializer.validated_data.get("email"))

            cache.set(
                f"{serializer.validated_data.get(
                'email')}ngo",
                otp,
                timeout=600,
            )
            return responseModel(
                {
                    "message": gettext("userRegistersuccessfully"),
                },
                msg=gettext("userRegistersuccessfully"),
            )

        return responseModel(
            status=False,
            msg=errorMsg(serializer.errors),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, *args, **kwargs):

        ngoDetail = request.user

        if ngoDetail:
            serializer = NgoDetailStep1Serializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.update(
                    instance=ngoDetail, validated_data=serializer.validated_data
                )

                return responseModel(
                    status=True, msg=gettext("stepOneSuccessfullyUpdated")
                )
        return responseModel(
            status=False,
            msg=errorMsg("UserDetailNotExist"),
            data="UserDetailNotExist",
            statusCode=status.HTTP_400_BAD_REQUEST,
        )


class NGORegistrationStep2View(NGOBaseAuthAPIView):

    except_token_Api_method = ["POST"]

    def get(self, request, *args, **kwargs):

        user = request.user

        if user:
            return responseModel(
                status=True, data=NgoDetailStep2Serializer(instance=user).data
            )
        return responseModel(
            status=False,
            msg=errorMsg("UserDetailNotExist"),
            data="UserDetailNotExist",
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def post(self, request):
        if not request.content_type.startswith("multipart/form-data"):
            return responseModel(
                status=False,
                msg=errorMsg("Multipart/form-data content type required."),
                data="Multipart/form-data content type required.",
                statusCode=status.HTTP_400_BAD_REQUEST,
            )

        serializer = NgoDetailStep2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.update(
                instance=NGODetailModel.objects.get(id=verifyAccessToken(request)),
                validated_data=serializer.validated_data,
            )
            return responseModel(
                {"message": gettext("registrationStepTwoCompleted")},
                msg=gettext("registrationStepTwoCompleted"),
            )

        return responseModel(
            status=False,
            msg=errorMsg(serializer.errors),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, *args, **kwargs):

        ngoDetail = request.user

        serializer = NgoDetailStep2Serializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(
                instance=ngoDetail, validated_data=serializer.validated_data
            )

            return responseModel(status=True, msg=gettext("stepTwoSuccessfullyUpdated"))


class NGORegistrationStep3View(NGOBaseAuthAPIView):
    except_token_Api_method = ["POST"]

    def get(self, request, *args, **kwargs):

        user = request.user

        if user:
            return responseModel(
                status=True, data=NgoDetailStep3Serializer(instance=user).data
            )
        return responseModel(
            status=False,
            msg=errorMsg("UserDetailNotExist"),
            data="UserDetailNotExist",
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def post(self, request):

        serializer = NgoDetailStep3Serializer(data=request.data)

        if serializer.is_valid():
            serializer.update(
                instance=NGODetailModel.objects.get(id=verifyAccessToken(request)),
                validated_data=serializer.validated_data,
            )
            return responseModel(
                {"message": gettext("registrationStepThreeCompleted")},
                msg=gettext("registrationStepThreeCompleted"),
            )

        return responseModel(
            status=False,
            msg=errorMsg(serializer.errors),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, *args, **kwargs):

        ngoDetail = request.user

        serializer = NgoDetailStep3Serializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(
                instance=ngoDetail, validated_data=serializer.validated_data
            )
            return responseModel(
                status=True, msg=gettext("stepThreeSuccessfullyUpdated")
            )


class OTPVerificationView(NGOBaseAuthAPIView):
    except_token_Api_method = ["POST"]

    def post(self, request, *args, **kwargs):
        otpSerializer = OTPSerializer(data=request.data)
        if otpSerializer.is_valid():
            cached_otp = cache.get(otpSerializer.validated_data["email"] + "ngo")

            if cached_otp is None:
                return responseModel(
                    {"message": "OTP has expired or not generated yet."},
                    status=False,
                    statusCode=status.HTTP_400_BAD_REQUEST,
                )

            if otpSerializer.validated_data["otp"] == cached_otp:
                ngo_detail = NGODetailModel.objects.get(
                    email=otpSerializer.validated_data["email"]
                )
                ngo_detail.is_verified = True
                ngo_detail.save()

                cache.delete(otpSerializer.validated_data["email"])
                return responseModel(
                    {
                        "message": "OTP verified successfully.",
                        "token": getToken(user=ngo_detail),
                    },
                    statusCode=status.HTTP_200_OK,
                )
            else:

                return responseModel(
                    {"message": "Incorrect OTP entered."},
                    status=False,
                    statusCode=status.HTTP_400_BAD_REQUEST,
                )

        return responseModel(
            status=False,
            data=otpSerializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )


class LoginView(NGOBaseAuthAPIView):
    except_token_Api_method = ["POST"]

    def post(self, request):
        loginSerializer = LoginSerializer(data=request.data)

        if loginSerializer.is_valid():

            user = NGODetailModel.objects.get(
                email=loginSerializer.validated_data["email"]
            )

            if user.password == loginSerializer.validated_data["password"]:
                if user.is_verified:

                    return responseModel(
                        {
                            "message": gettext("SuccessfulLogin"),
                            "isVerify": True,
                            "token": getToken(user=user),
                        },
                        status=True,
                        msg=gettext("SuccessfulLogin"),
                        statusCode=status.HTTP_200_OK,
                    )
                else:
                    otp = generate_otp()
                    subject = "Daan-i OTP Verification"
                    message = f"Your OTP Is {otp}"
                    sendEmail(
                        subject, message, loginSerializer.validated_data.get("email")
                    )
                    cache.set(
                        f"{loginSerializer.validated_data.get(
                        'email')}ngo",
                        otp,
                        timeout=600,
                    )
                    return responseModel(
                        {
                            "message": gettext(
                                "YourAccountIsNotVerified.AndOTPHasBeenSentatGmail"
                            ),
                            "isVerify": False,
                        },
                        status=False,
                        msg=gettext(
                            "YourAccountIsNotVerified.AndOTPHasBeenSentatGmail"
                        ),
                        statusCode=status.HTTP_400_BAD_REQUEST,
                    )

            else:
                return responseModel(
                    {
                        "message": gettext("PasswordIncorrect"),
                    },
                    status=False,
                    msg=gettext("PasswordIncorrect"),
                    statusCode=status.HTTP_400_BAD_REQUEST,
                )

        return responseModel(
            status=False,
            msg=errorMsg(loginSerializer.errors),
            data=loginSerializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )


def generate_otp():
    otp = random.randint(1000, 9999)
    return otp
