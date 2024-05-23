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
from .views.user_auth_views import *
from .views.address_views import *

urlpatterns = [
    path("signup", UserRegistrationView.as_view(), name="Donar Signup"),
    path("otpVerify", OTPVerificationView.as_view(), name="Donar OTP Verification"),
    path("login", LoginView.as_view(), name="Donar Login"),
    path("address", AddressView.as_view(), name="Address"),
    path("address/<int:id>", AddressView.as_view(), name="Address with Id"),
]
