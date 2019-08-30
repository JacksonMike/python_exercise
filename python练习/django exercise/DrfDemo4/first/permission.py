from rest_framework.permissions import BasePermission


class MyPermission(object):
    message = "权限不够"

    def has_permission(self, request, view):
        user_obj = request.user
        if user_obj.kind == 1:
            return False
        else:
            return True
