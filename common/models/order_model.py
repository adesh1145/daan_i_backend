from django.db import models

from common.models.category_model import CategoryModel

# from common.models.order_address_model import OrderAddressModel
from donar.models.user_model import UserDetailModel
from ngo.models.ngo_user_model import NGODetailModel


class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(
        CategoryModel,
        related_name="order_category",
        on_delete=models.CASCADE,
    )
    weight = models.FloatField(
        default=0.0,
    )
    description = models.CharField(max_length=255, null=True)

    donar = models.ForeignKey(
        UserDetailModel,
        related_name="order_donar",
        on_delete=models.CASCADE,
    )

    ngo = models.ForeignKey(
        NGODetailModel, related_name="order_ngo", on_delete=models.CASCADE, blank=True
    )

    order_status = models.CharField(
        max_length=50,
        choices=[
            ("ongoing", "Ongoing"),
            ("booked", "Booked"),
            ("accept", "Accepted"),
            ("complete", "Completed"),
            ("cancel", "Cancelled"),
        ],
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )  # Automatically set on creation
    updated_date = models.DateTimeField(auto_now=True)  # Automatically set on update

    class Meta:
        db_table = "order"
        verbose_name = "Order Table"  # Change the display name for a single object
        verbose_name_plural = "Order Table"


class OrderImage(models.Model):
    order = models.ForeignKey(
        OrderModel, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="order_images/")
