from django.template import Library

register = Library()


@register.inclusion_tag("web/menu.html")
def get_menu_style():
    menu_list = [1, 2, 3]
    return {"menu_list": menu_list}
