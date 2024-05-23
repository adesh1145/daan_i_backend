from django.db import models


class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'  # Change the display name for a single object
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def __unicode__(self):
        return self.category_name
