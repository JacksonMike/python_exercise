from django.template import Library
import re

register = Library()


@register.inclusion_tag("rbac/menu.html")
def get_menu_style(request):
    permissions_menu_dict = request.session.get("permissions_menu_dict")
    print(permissions_menu_dict)
    for val in permissions_menu_dict.values():
        for item in val["children"]:
            val["class"] = "hide"
            if request.show_id == item["pk"]:
                val["class"] = ""
    return {"permissions_menu_dict": permissions_menu_dict}


@register.filter
def has_permission(btn_url, request):
    permissions__name = request.session.get("permissions__name")
    return btn_url in permissions__name
