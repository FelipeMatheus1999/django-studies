# Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Local
from apps.account.models import AccountModel


@admin.register(AccountModel)
class AccountAdmin(admin.ModelAdmin):
    exclude = ["password"]
    list_display = ["username", "email", "last_login", "date_joined", "is_active"]
    readonly_fields = [
        "id",
        "username", 
        "first_name",
        "last_name",
        "email",
        "picture",
        "is_active",
        "date_joined",
        "last_login",
    ]
    filter_horizontal = ["groups"]
    fieldsets = [
        (
            _("Identification"),
            {
                "fields": [
                    "id",
                    "username", 
                    "first_name",
                    "last_name",
                    "email",
                    "picture",
                ],
            },
        ),
        (
            _("Interaction"),
            {
                "fields": [
                    "is_active",
                    "date_joined",
                    "last_login",
                ]
            },
        ),
    ]
