from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
    Returns the string split by the specified delimiter
    Usage: {{ "a,b,c"|split:"," }} -> ['a', 'b', 'c']
    """
    return value.split(key)