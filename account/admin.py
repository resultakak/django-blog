from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUserModel


class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Change Avatar Area', {
            'fields': ['avatar']
        }),
    )


admin.site.register(CustomUserModel, CustomAdmin)
