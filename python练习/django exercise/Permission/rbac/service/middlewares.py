from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
import re


class PermissionMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        current_path = request.path

        for reg in ["/enter/", "/admin/*"]:
            ret = re.search(reg, current_path)
            if ret:
                return None
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("/enter/")

        permissions_list = request.session.get("permissions_list")
        for reg in permissions_list:
            reg_limit = "^%s$" % reg
            ret = re.search(reg_limit, current_path)
            if ret:
                return None
        return HttpResponse("没有访问权限")
