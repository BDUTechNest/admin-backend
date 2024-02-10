from django.contrib import admin
from apps.users.models.user import User
from apps.users.models.division_admin import DivisionalAdmin
from apps.users.models.division_authority import DivisionalAuthority
from apps.users.models.national_admin import NationalAdmin
from apps.users.models.national_authority import NationalAuthority
from django.contrib.admin import ModelAdmin


@admin.register(User)
class DivisionalAdminView(ModelAdmin):
    list_display = ["email", "role", "groups"]


admin.site.register(DivisionalAdmin)
admin.site.register(NationalAdmin)
admin.site.register(NationalAuthority)
admin.site.register(DivisionalAuthority)
