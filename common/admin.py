from django.contrib import admin

from common.models.banner_model import BannerModel

# from common.models.order_address_model import OrderAddressModel
from common.models.order_model import OrderImage, OrderModel

from .models.state_city_models import StateModel, CityModel
from .models.category_model import CategoryModel


class StateAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = [
        "id",
        "name",
    ]
    search_fields = ["id", "name"]


class CityAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = ["id", "name"]
    search_fields = ["id", "name"]


class CategoryAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = [
        "id",
        "category_name",
    ]
    search_fields = ["id", "category_name"]


admin.site.register(StateModel, StateAdmin)
admin.site.register(CityModel, CityAdmin)
admin.site.register(CategoryModel, CategoryAdmin)


class OrderImageInline(admin.TabularInline):
    model = OrderImage
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id", "donar", "ngo", "order_status"]
    list_filter = ["order_status"]
    search_fields = ["order_id", "id"]
    inlines = [
        OrderImageInline,
    ]


class OrderImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "order",
    ]

    search_fields = ["id"]


admin.site.register(OrderModel, OrderAdmin)
admin.site.register(OrderImage, OrderImageAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]


admin.site.register(BannerModel, BannerAdmin)
