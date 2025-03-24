from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import CustomManager

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'phone_number')

    fieldsets = (
        (None, {'fields': ('phone_number', 'username', 'password')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    objects = CustomManager()
    ordering = ('phone_number',)

admin.site.register(CustomUser, CustomUserAdmin)