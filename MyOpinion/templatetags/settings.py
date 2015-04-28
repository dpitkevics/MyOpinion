from django import template
from django.conf import settings
from django.utils.translation import ugettext as _

from MyOpinion.settings import APP_NAME

register = template.Library()


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")


@register.assignment_tag(takes_context=True)
def settings_context(context, name):
    return settings_value(name)

@register.simple_tag
def title(title_text=''):
    if len(title_text) > 0:
        return "%s - %s" % (_(title_text), APP_NAME)

    return APP_NAME