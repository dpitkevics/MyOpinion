from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic, TopicTag, TopicCategory


def index(request):
    topic_list = Topic.objects.all()[:5]

    context = {
        'topic_list': topic_list,
    }

    return render(request, 'Topics/index.html', context)


def view_topic(request, slug):
    try:
        topic = Topic.objects.get(slug=slug)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, _('Topic not found'))

        return HttpResponseRedirect(reverse('Topics:index'))

    context = {
        'topic': topic,
    }

    return render(request, 'Topics/view_topic.html', context)


def topics_by_tag(request, slug):
    topic_tag = TopicTag.objects.get(slug=slug)

    topic_list = topic_tag.topics.all()

    context = {
        'topic_tag': topic_tag,
        'topic_list': topic_list,
    }

    return render(request, 'Topics/topics_by_tag.html', context)


def topics_by_category(request, slug):
    topic_category = TopicCategory.objects.get(slug=slug)

    topic_list = topic_category.topic_set.all()

    context = {
        'topic_category': topic_category,
        'topic_list': topic_list,
    }

    return render(request, 'Topics/topics_by_category.html', context)