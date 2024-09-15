# Create your views here.

from daan_i_backend.utils.response_model import errorMsg
from donar.views.custom_base_auth_apiview import DonarBaseAuthAPIView
from ..common_imports import *


from ..serializers.user_detail_serializer import *

from ..models.user_model import UserDetailModel


from rest_framework.permissions import AllowAny


class UserRegistrationView(DonarBaseAuthAPIView):
    except_token_Api_method = ["POST"]

    def get(self, request, *args, **kwargs):

        user = request.user

        if user:
            return responseModel(
                status=True, data=UserDetailSerializer(instance=user).data
            )
        return responseModel(
            status=False,
            msg=errorMsg("UserDetailNotExist"),
            data="UserDetailNotExist",
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def post(self, request):
        serializer = UserDetailSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            otp = generate_otp()
            print(otp)
            subject = "Daan-i OTP Verification"
            message = f"Your OTP Is {otp}"
            cache.set(
                serializer.validated_data.get("email") + "donar", otp, timeout=600
            )
            try:
                sendEmail(subject, message, serializer.validated_data.get("email"))
            except Exception as e:
                pass

            return responseModel(
                {"message": gettext("OtpHasBeenSentYourEmail")},
                msg=gettext("OtpHasBeenSentYourEmail"),
            )
        return responseModel(
            status=False,
            msg=errorMsg(serializer.errors),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, *args, **kwargs):
        if not request.content_type.startswith("multipart/form-data"):
            return responseModel(
                status=False,
                msg=errorMsg("Multipart/form-data content type required."),
                data="Multipart/form-data content type required.",
                statusCode=status.HTTP_400_BAD_REQUEST,
            )
        donarDetail = request.user

        serializer = UserDetailSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(
                validated_data=serializer.validated_data, instance=donarDetail
            )

            return responseModel(status=True, msg=gettext("profileUpdated"))
        return responseModel(
            status=False,
            msg=gettext(
                errorMsg(serializer.errors),
            ),
            data=serializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )


def generate_otp():
    otp = random.randint(1000, 9999)
    return otp


class OTPVerificationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        otpSerializer = OTPSerializer(data=request.data)
        if otpSerializer.is_valid():
            cached_otp = cache.get(otpSerializer.validated_data["email"] + "donar")
            print(cached_otp)
            if cached_otp is None:
                return responseModel(
                    msg="OTP has expired or not generated yet.",
                    data={"message": "OTP has expired or not generated yet."},
                    status=False,
                    statusCode=status.HTTP_400_BAD_REQUEST,
                )

            if otpSerializer.validated_data["otp"] == cached_otp:
                user_detail = UserDetailModel.objects.get(
                    email=otpSerializer.validated_data["email"]
                )
                user_detail.isVerified = True
                user_detail.save()

                cache.delete(otpSerializer.validated_data["email"] + "donar")
                return responseModel(
                    {
                        "message": "OTP verified successfully.",
                        "token": getToken(user=user_detail),
                    },
                    statusCode=status.HTTP_200_OK,
                )
            else:

                return responseModel(
                    {"message": "Incorrect OTP entered."},
                    status=False,
                    msg="Incorrect OTP entered.",
                    statusCode=status.HTTP_400_BAD_REQUEST,
                )

        return responseModel(
            status=False,
            msg=errorMsg(otpSerializer.errors),
            data=otpSerializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        loginSerializer = LoginSerializer(data=request.data)

        if loginSerializer.is_valid():

            user = UserDetailModel.objects.get(
                email=loginSerializer.validated_data["email"]
            )

            if user.password == loginSerializer.validated_data["password"]:
                if user.isVerified:

                    return responseModel(
                        {
                            "message": "Successful Login",
                            "isVerify": True,
                            "token": getToken(user=user),
                        },
                        status=True,
                        msg="Successful Login",
                        statusCode=status.HTTP_200_OK,
                    )
                else:
                    otp = generate_otp()
                    subject = "Daan-i OTP Verification"
                    message = f"Your OTP Is {otp}"
                    try:
                        sendEmail(
                            subject,
                            message,
                            loginSerializer.validated_data.get("email"),
                        )
                    except Exception as e:
                        pass

                    cache.set(
                        f"{loginSerializer.validated_data.get('email')}",
                        otp,
                        timeout=600,
                    )
                    return responseModel(
                        {"message": "Your Account Is Not Verified", "isVerify": False},
                        status=False,
                        msg="Your Account Is Not Verified",
                        statusCode=status.HTTP_400_BAD_REQUEST,
                    )

            else:
                return responseModel(
                    {"message": "Password Incorrect"},
                    status=False,
                    msg="Password Incorrect",
                    statusCode=status.HTTP_400_BAD_REQUEST,
                )

        return responseModel(
            status=False,
            msg=errorMsg(loginSerializer.errors),
            data=loginSerializer.errors,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )
