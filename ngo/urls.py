"""daan_i_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from ngo.views.my_donation_views import MyDonationView
from ngo.views.ngo_auth_views import *

urlpatterns = [
    path("signupStepOne", NGORegistrationStep1View.as_view(), name="NGO Signup Step 1"),
    path("signupStepTwo", NGORegistrationStep2View.as_view(), name="NGO Signup Step 2"),
    path(
        "signupStepThree", NGORegistrationStep3View.as_view(), name="NGO Signup Step 3"
    ),
    path("otpVerify", OTPVerificationView.as_view(), name="NGO OTP Verification"),
    path("login", LoginView.as_view(), name="NGO Login"),
    path("myDonation", MyDonationView.as_view(), name="My Donation List"),
    path("myDonation/<int:id>", MyDonationView.as_view(), name="My Donation List"),
]
