from django.db import models


class BannerModel(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()

    class Meta:
        db_table = "banner"
        verbose_name = "Banner"  # Change the display name for a single object
        verbose_name_plural = "banners"

    def __str__(self):
        return f"{self.id}"
