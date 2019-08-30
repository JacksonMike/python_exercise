from django.contrib import admin
from first.models import *


# Register your models here.
class UserConfig(admin.ModelAdmin):
    list_display = ["pk", "name"]
    ordering = ["pk"]


admin.site.register(User, UserConfig)


class RoleConfig(admin.ModelAdmin):
    list_display = ["pk", "title"]
    ordering = ["pk"]


admin.site.register(Role, RoleConfig)


class PermissionConfig(admin.ModelAdmin):
    list_display = ["pk", "title", "url"]
    ordering = ["pk"]


admin.site.register(Permission, PermissionConfig)
