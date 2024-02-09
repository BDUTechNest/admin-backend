from django.contrib import admin
from .models.user import User
from .models.division_admin import DivisionalAdmin
from .models.division_authority import DivisionalAuthority
from .models.national_admin import NationalAdmin
from .models.national_authority import NationalAuthority
from django.contrib.admin import ModelAdmin


@admin.register(User)
class DivisionalAdminView(ModelAdmin):
    list_display = ["email", "role", "groups"]


admin.site.register(DivisionalAdmin)
admin.site.register(NationalAdmin)
admin.site.register(NationalAuthority)
admin.site.register(DivisionalAuthority)
