from django.db import models
from common.models.state_city_models import CityModel, StateModel
from donar.models.user_model import UserDetailModel


class AddressModel(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    address = models.CharField(max_length=255, blank=True)
    landmark = models.CharField(max_length=255, blank=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    state = models.ForeignKey(
        StateModel,
        related_name="state",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        CityModel, related_name="city", on_delete=models.CASCADE, blank=True, null=True
    )
    user = models.ForeignKey(
        UserDetailModel,
        related_name="donar",
        on_delete=models.CASCADE,
    )
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        auto_now_add=True
    )  # Automatically set on creation
    updated_date = models.DateTimeField(auto_now=True)  # Automatically set on update

    class Meta:
        db_table = "donar_address"
        verbose_name = "Donar Address"  # Change the display name for a single object
        verbose_name_plural = "Donar Address"
