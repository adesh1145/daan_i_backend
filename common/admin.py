from django.contrib import admin

from common.models.order_address_model import OrderAddressModel
from common.models.order_model import OrderImage, OrderModel

from .models.state_city_models import StateModel, CityModel
from .models.category_model import CategoryModel


class StateAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = [
        "id",
        "name",
    ]


class CityAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = ["id", "name"]


class CategoryAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = [
        "id",
        "category_name",
    ]


class OrderAddressAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = ["id", "address", "city", "state"]


admin.site.register(StateModel, StateAdmin)
admin.site.register(CityModel, CityAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(OrderAddressModel, OrderAddressAdmin)


class OrderImageInline(admin.TabularInline):
    model = OrderImage
    extra = 1


class OrderAddressInline(admin.TabularInline):
    model = OrderAddressModel
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id", "donar", "ngo", "order_status"]
    list_filter = ["order_status"]
    search_fields = ["order_id"]
    inlines = [OrderImageInline, OrderAddressInline]


admin.site.register(OrderModel, OrderAdmin)
admin.site.register(OrderImage)
