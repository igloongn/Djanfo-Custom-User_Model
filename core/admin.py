from django.contrib import admin
from core.models import CustomUser
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    model = CustomUser
    ordering = ('-id',)
    list_display=('username', 'email', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'firstname')}),
        (('Permissions'), {'fields': ('is_staff', 'is_active')}),
        (('Personal'), {'fields': ('about', )}),
    )
    # list_display=('email', 'username', 'firstname', 'is_active', 'is_staff')




admin.site.register(CustomUser, UserAdminConfig)