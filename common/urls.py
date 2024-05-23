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
from .views.category_views import CategoryView
from .views.state_city_views import StateView, CityView


urlpatterns = [
    path("category", CategoryView.as_view(), name="Category List"),
    path("state", StateView.as_view(), name="State List"),
    path("city", CityView.as_view(), name="City List"),
]
