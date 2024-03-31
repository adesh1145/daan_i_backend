from rest_framework_simplejwt.tokens import *
from datetime import timedelta
from django.db import models


def getToken(user: models.Model, refresh_exp=timedelta(days=30), access_exp=timedelta(days=1)) -> Dict:
    refresh_token = RefreshToken.for_user(
        user=user,)

    refresh_token.set_exp(lifetime=refresh_exp)
    access_token = AccessToken(str(refresh_token.access_token))
    access_token.set_exp(lifetime=access_exp)
    return {
        'accessToken': str(access_token),
        'refreshToken': str(refresh_token)
    }


def verifyAccessToken(token: str) -> int:
    try:
        accessToken = AccessToken(token=token)
        return accessToken.payload['user_id']
    except Exception as e:
        return 0
