from django.db import models


class StateModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'State'
        verbose_name = 'State'  # Change the display name for a single object
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name


class CityModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(
        StateModel, related_name='cities', on_delete=models.CASCADE)

    class Meta:
        db_table = 'City'
        verbose_name = 'City'  # Change the display name for a single object
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
