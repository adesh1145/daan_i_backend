from django.db import models


class UserDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    isVerified = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True)  # Automatically set on creation
    updated_date = models.DateTimeField(
        auto_now=True)  # Automatically set on update
    profile_image = models.ImageField(blank=True)  # Store image URL
    address = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'donar_user_detail'
        verbose_name = 'User Detail'  # Change the display name for a single object
        verbose_name_plural = 'Users Detail'

    def __str__(self):
        return self.name
