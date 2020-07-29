from django import template

register = template.Library()

@register.filter
def verbose_name(obj, field):
    print(obj, field)
    return obj._meta.get_field(field).verbose_name
@register.filter
def percantage(num, num_total):
    try:

        print(num)
        print(num_total)
        return round(float((int(num)*100) / int(num_total)),2)
    except ValueError:
        return 0
    except ZeroDivisionError:
        return 0
