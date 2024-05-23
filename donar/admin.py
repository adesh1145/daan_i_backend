from django.contrib import admin

from donar.models.address_model import AddressModel

from .models.user_model import UserDetailModel


class DonarUserAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = ['id', 'name', 'email', 'isVerified']
    readonly_fields = ['id', 'created_date', 'updated_date', 'isVerified']


class AddressAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = ['id', 'address', 'city', 'state', 'is_default']


admin.site.register(UserDetailModel, DonarUserAdmin)
admin.site.register(AddressModel, AddressAdmin)
