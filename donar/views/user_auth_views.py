
# Create your views here.

from ..common_imports import *


from ..serializers.user_detail_serializer import *

from ..models.user_model import UserDetailModel
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from datetime import timedelta


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserDetailSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            otp = generate_otp()
            subject = 'Daan-i OTP Verification'
            message = f'Your OTP Is {otp}'
            sendEmail(subject, message,
                      serializer.validated_data.get('email'))

            cache.set(serializer.validated_data.get('email'), otp, timeout=600)
            return ResponseModel({

                "message": gettext("userRegistersuccessfully")
            },
                msg=gettext("userRegistersuccessfully")

            )
        return ResponseModel(
            status=False,
            data=serializer.errors, statusCode=status.HTTP_400_BAD_REQUEST)


def generate_otp():
    otp = random.randint(1000, 9999)
    return otp


class OTPVerificationView(APIView):
    def post(self, request, *args, **kwargs):
        otpSerializer = OTPSerializer(data=request.data)
        if otpSerializer.is_valid():
            cached_otp = cache.get(
                otpSerializer.validated_data['email'])

            if cached_otp is None:
                return ResponseModel({'message': 'OTP has expired or not generated yet.'}, status=False, statusCode=status.HTTP_400_BAD_REQUEST)

            if otpSerializer.validated_data['otp'] == cached_otp:
                user_detail = UserDetailModel.objects.get(
                    email=otpSerializer.validated_data['email'])
                user_detail.isVerified = True
                user_detail.save()

                cache.delete(otpSerializer.validated_data['email'])
                return ResponseModel({'message': 'OTP verified successfully.'}, statusCode=status.HTTP_200_OK)
            else:

                return ResponseModel({'message': 'Incorrect OTP entered.'}, status=False, statusCode=status.HTTP_400_BAD_REQUEST)

        return ResponseModel(
            status=False,
            data=otpSerializer.errors, statusCode=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):

        loginSerializer = LoginSerializer(data=request.data)

        if loginSerializer.is_valid():

            user = UserDetailModel.objects.get(
                email=loginSerializer.validated_data['email'])

            if user.password == loginSerializer.validated_data['password']:
                if user.isVerified:

                    return ResponseModel(
                        {
                            'message': "Successful Login",
                            'isVerify': True,
                            'token': getToken(user=user)
                        },
                        status=True,
                        msg="Successful Login",
                        statusCode=status.HTTP_200_OK
                    )
                else:
                    otp = generate_otp()
                    subject = 'Daan-i OTP Verification'
                    message = f'Your OTP Is {otp}'
                    sendEmail(subject, message,
                              loginSerializer.validated_data.get('email'))

                    return ResponseModel(
                        {
                            'message': "Your Account Is Not Verified",
                            'isVerify': False
                        },
                        status=False,
                        msg="Your Account Is Not Verified",
                        statusCode=status.HTTP_400_BAD_REQUEST
                    )

            else:
                return ResponseModel(
                    {
                        'message': "Password Incorrect"
                    },
                    status=False,
                    msg="Password Incorrect",
                    statusCode=status.HTTP_400_BAD_REQUEST
                )

        return ResponseModel(
            status=False,
            msg="Error",
            data=loginSerializer.errors, statusCode=status.HTTP_400_BAD_REQUEST)
