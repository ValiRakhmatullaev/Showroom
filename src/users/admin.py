from django.contrib import admin

from src.users.models import ShowroomUser


@admin.register(ShowroomUser)
class ShowroomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "is_producer",
        "is_customer",
        "is_showroom",
    )
