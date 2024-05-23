from rest_framework.authentication import BaseAuthentication
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from daan_i_backend.utils.jwt_token import verifyAccessToken
from ngo.models.ngo_user_model import NGODetailModel
from rest_framework_simplejwt.exceptions import (
    AuthenticationFailed,
    TokenError,
    InvalidToken,
    TokenBackendError,
)
from rest_framework.exceptions import ErrorDetail


class NGOBaseAuthAPIView(APIView):
    except_token_Api_method = [str]
    authentication_classes = []
    permission_classes = []

    def get_authenticators(self):
        if self.request.method in self.except_token_Api_method:
            return []
        return [NGOJWTAuthentication()]

    def get_permissions(self):
        if self.request.method in self.except_token_Api_method:
            return [AllowAny()]
        return []


class NGOJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise AuthenticationFailed(
                detail="Token Required",
                code=status.HTTP_400_BAD_REQUEST,
            )

        try:
            ngo_user_id = verifyAccessToken(request=request)

            ngo_user = NGODetailModel.objects.get(id=ngo_user_id)
        except TokenError:
            raise InvalidToken(
                detail="Token is invalid or expired", code=status.HTTP_401_UNAUTHORIZED
            )
        except NGODetailModel.DoesNotExist:
            raise AuthenticationFailed(
                detail="Data Not Found", code=status.HTTP_404_NOT_FOUND
            )

        return (ngo_user, None)
