from django.contrib import admin
from .models.user import User
from .models.divisionadmin import DivisionalAdmin
from .models.divisionauthority import DivisionalAuthority
from .models.nationaladmin import NationalAdmin
from .models.nationalauthority import NationalAuthority
from django.contrib.admin import ModelAdmin


@admin.register(User)
class DivisionalAdminView(ModelAdmin):
    list_display = ["email", "role", "groups"]


admin.site.register(DivisionalAdmin)
admin.site.register(NationalAdmin)
admin.site.register(NationalAuthority)
admin.site.register(DivisionalAuthority)
