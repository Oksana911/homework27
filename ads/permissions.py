from rest_framework.permissions import BasePermission
from ads.models import Selection
from users.models import User


class SelectionUpdatePermission(BasePermission):
    message = "Only selection's author can update/delete selection"

    # def has_permission(self, request, view):
    #     if request.user == Selection.author:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class AdUpdatePermission(BasePermission):
    message = "Only ad's author can update/delete ad"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [User.ROLES[1][1], User.ROLES[2][1]]:
            return True
        return False
