from django.contrib import admin

from core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    exclude = ('password', )
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(User, UserAdmin)
