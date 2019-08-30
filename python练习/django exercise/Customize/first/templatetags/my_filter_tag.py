from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.filter
def mul(x, y):
    return x * y


"""
'first.apps.FirstConfig',
'second.apps.SecondConfig'
自定义过滤器如果同名,先找second的my_filter,再去first

渲染模版时候,全局没有则按照first, second的顺序去渲染
"""


@register.filter
def tag(val):
    return mark_safe("<h1>%s</h1>" % val)


@register.filter
def upper(val):
    return val.upper()


@register.simple_tag
def mul_tag(x, y, z):
    return x * y * z


@register.inclusion_tag("menu.html")
def get_menu():
    lst = [1, 3, 5]
    return {"lst": lst}