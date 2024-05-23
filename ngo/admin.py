from django.contrib import admin

from .models.ngo_user_model import NGODetailModel, NGODetailForm
from .serializers.ngo_detail_serializer import NgoDetailStep1Serializer


class NGOUserAdmin(admin.ModelAdmin):
    # Display these fields in the admin panel
    list_display = ["id", "ngo_name", "email", "mobile", "is_verified"]
    readonly_fields = ["id", "created_date", "updated_date", "is_verified"]
    form = NGODetailForm


admin.site.register(NGODetailModel, NGOUserAdmin)
