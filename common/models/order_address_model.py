from django.db import models
from common.models.order_model import OrderModel
from common.models.state_city_models import CityModel, StateModel


class OrderAddressModel(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
        OrderModel, related_name="address", on_delete=models.CASCADE
    )
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    address = models.CharField(max_length=255, blank=True)
    landmark = models.CharField(max_length=255, blank=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    state = models.ForeignKey(
        StateModel,
        related_name="order_state",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        CityModel,
        related_name="order_city",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    addres_type = models.CharField(
        max_length=255,
        choices=[
            ("pickup_address", "PickUp Address"),
            ("drop_address", "Drop Address"),
        ],
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )  # Automatically set on creation
    updated_date = models.DateTimeField(auto_now=True)  # Automatically set on update

    class Meta:
        db_table = "order_address"
        verbose_name = "Order Address"  # Change the display name for a single object
        verbose_name_plural = "Order Address"
