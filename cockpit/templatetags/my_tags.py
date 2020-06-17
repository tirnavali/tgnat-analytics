from django import template

register = template.Library()

@register.filter
def verbose_name(obj, field):
    print(obj, field)
    return obj._meta.get_field(field).verbose_name