from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsCustomerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and getattr(request.user, "is_customer", None)
        )


class IsShowroomUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and getattr(request.user, "is_showroom", None)
        )


class IsProducerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and getattr(request.user, "is_producer", None)
        )
