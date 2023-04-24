from django import template 
register = template.Library()  

@register.simple_tag 
def defined(val=None):
    return val