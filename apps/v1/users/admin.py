from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.v1.shared.admin import BaseAdmin
from .models import User, UserConfirmation

class UserResource(resources.ModelResource):
    class Meta:
        model = User


class UserConfirmationResource(resources.ModelResource):
    class Meta:
        model = UserConfirmation


class UserModelAdmin(ImportExportModelAdmin, BaseAdmin, UserAdmin):
    resource_classes = [UserResource]
    list_display = [f.name for f in User._meta.fields if f.name not in ('password', 'groups', 'user_permissions', 'is_staff', 'is_superuser')]


class UserConfirmationAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [UserConfirmationResource]
    list_display = [f.name for f in UserConfirmation._meta.fields]


admin.site.register(User, UserModelAdmin)
admin.site.register(UserConfirmation, UserConfirmationAdmin)