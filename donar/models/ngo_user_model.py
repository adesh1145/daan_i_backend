import os
from django import forms
from django.db import models
from common.models.category_model import CategoryModel
from common.models.state_city_models import StateModel, CityModel

# def upload_ngo_image(instance, filename):
#     # Define the path where you want to store the image
#     upload_path = os.path.join('ngo_images', instance.ngo_name)
#     # Return the full path including the filename
#     return os.path.join(upload_path, filename)


class NGODetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    ngo_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    t_and_c_status = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True
    )  # Automatically set on creation
    updated_date = models.DateTimeField(auto_now=True)  # Automatically set on update
    registration_step = models.IntegerField(default=1)
    ngo_image = models.ImageField(
        blank=True,
    )  # Store image URL
    reg_certificate_image = models.ImageField(blank=True)  # Store image URL
    pan_card_image = models.ImageField(blank=True)  # Store image URL
    ngo_owner_ame = models.CharField(max_length=100, blank=True)
    reg_certificate_no = models.CharField(max_length=255, blank=True)
    pan_no = models.CharField(max_length=255, blank=True)
    gst_no = models.CharField(max_length=255, blank=True)
    accept_category = models.ManyToManyField(
        CategoryModel,
    )
    address = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    landmark = models.CharField(max_length=255, blank=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    state = models.ForeignKey(
        StateModel,
        related_name="users",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        CityModel, related_name="users", on_delete=models.CASCADE, blank=True, null=True
    )
    # Assuming you want to store the city of the user

    class Meta:
        db_table = "ngo_user_detail"
        verbose_name = "NGO User Detail"  # Change the display name for a single object
        verbose_name_plural = "NGO Users Detail"

    def __str__(self):
        return self.ngo_name


# forms.py


class NGODetailForm(forms.ModelForm):
    class Meta:
        model = NGODetailModel
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("state") and cleaned_data.get("city"):

            if not CityModel.objects.filter(
                id=cleaned_data.get("city").id, state=cleaned_data.get("state")
            ).exists():

                raise forms.ValidationError(
                    message=f"{cleaned_data.get('city').name} is Not Exist in {cleaned_data.get('state').name}"
                )
        return cleaned_data
