
from rest_framework.views import APIView
from rest_framework import status
from .response_model import ResponseModel
from django.utils.translation import gettext
import random
from django.core.cache import cache
from daan_i_backend.utils.send_email import sendEmail
from daan_i_backend.utils.jwt_token import *
