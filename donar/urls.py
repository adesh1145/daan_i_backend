"""""
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

from django.urls import path

from donar.views.donate_views import DonateView, DonationHistoryView
from donar.views.near_by_ngo_views import NearByNgoView
from donar.views.top_donar_views import TopDonorsView
from .views.user_auth_views import *
from .views.address_views import *

urlpatterns = [
    path("signup", UserRegistrationView.as_view(), name="Donar Signup"),
    path("otpVerify", OTPVerificationView.as_view(), name="Donar OTP Verification"),
    path("login", LoginView.as_view(), name="Donar Login"),
    path("address", AddressView.as_view(), name="Address"),
    path("address/<int:id>", AddressView.as_view(), name="Address with Id"),
    path("nearByNgo", NearByNgoView.as_view(), name="Near By NGO List"),
    path("donate", DonateView.as_view(), name="Donate"),
    path(
        "donateHistory/<int:id>",
        DonationHistoryView.as_view(),
        name="Donate History List",
    ),
    path(
        "donateHistory",
        DonationHistoryView.as_view(),
        name="Donate History List",
    ),
    path(
        "topDonar",
        TopDonorsView.as_view(),
        name="Top Donar List",
    ),
]
