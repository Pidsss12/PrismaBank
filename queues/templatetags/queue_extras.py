from django import template

register = template.Library()

@register.filter
def dict_key(d, k):
    return d.get(k, 0)
