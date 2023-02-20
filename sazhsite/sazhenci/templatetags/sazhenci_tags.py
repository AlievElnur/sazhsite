from django import template
from sazhenci.models import *

register = template.Library()

@register.simple_tag()
def get_left():
    return Left.objects.all()

@register.inclusion_tag('sazhenci/list_left.html')
def show_left():
    lefts = Left.objects.all()
    return {"lefts": lefts}