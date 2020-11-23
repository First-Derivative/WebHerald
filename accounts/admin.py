from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

class AccountAdminView(UserAdmin):
    list_display = ("id", "username", "email", "dob", "timestamp", "is_active", "is_admin")
    search_fields = ("id","username","email")
    readonly_fields = ("timestamp",)

    filter_horizontal = ()
    list_filter = ("is_admin",)
    fieldsets = ()

admin.site.register(Account,AccountAdminView)
