
from rest_framework.authentication import BaseAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from daan_i_backend.utils.jwt_token import verifyAccessToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError, InvalidToken, TokenBackendError

from ..models.user_model import UserDetailModel


class DonarBaseAuthAPIView(APIView):
    except_token_Api_method = [str]
    authentication_classes = []
    permission_classes = []

    def get_authenticators(self):
        if self.request.method in self.except_token_Api_method:
            return []
        return [DonarJWTAuthentication()]

    def get_permissions(self):
        if self.request.method in self.except_token_Api_method:
            return [AllowAny()]
        return []


class DonarJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            raise AuthenticationFailed(
                detail='Token Required', code=status.HTTP_400_BAD_REQUEST)

        try:
            ngo_user_id = verifyAccessToken(request=request)

            ngo_user = UserDetailModel.objects.get(id=ngo_user_id)
        except TokenError:
            raise InvalidToken(
                detail='Token is invalid or expired', code=status.HTTP_401_UNAUTHORIZED)
        except UserDetailModel.DoesNotExist:
            raise AuthenticationFailed(
                detail='Data Not Found', code=status.HTTP_404_NOT_FOUND)

        return (ngo_user, None)
