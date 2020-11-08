from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def build_date():
    return settings.BUILD_DATE
