from django.contrib import admin

from .models.user_model import UserDetailModel


class DonarUserAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = ['id', 'name', 'email', 'isVerified']
    readonly_fields = ['id', 'created_date', 'updated_date', 'isVerified']


admin.site.register(UserDetailModel, DonarUserAdmin)
