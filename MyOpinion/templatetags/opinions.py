from django import template

from Topics.models import TopicCategory

register = template.Library()


@register.simple_tag()
def get_category_list():
    topic_category_list = TopicCategory.objects.all()

    return topic_category_list


@register.assignment_tag(takes_context=True)
def get_category_list_context(context):
    return get_category_list()