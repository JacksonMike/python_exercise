from django.template import Library

register = Library()


@register.filter
def mul(x, y):
    return x * y + 1


@register.simple_tag
def tag(val):
    return "<h1>%s</h1>" % val
