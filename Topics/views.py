from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Disqus import DisqusAPI
from MyOpinion import settings

from MyOpinion.templatetags.templating import StaticFile

from .models import Topic, TopicTag, TopicCategory


def index(request):
    topic_list = Topic.objects.all()[:20]

    context = {
        'topic_list': topic_list,
    }

    return render(request, 'Topics/index.html', context)


def trending(request):
    disqus = DisqusAPI(settings.DISQUS_SECRET_KEY, settings.DISQUS_PUBLIC_KEY)
    popular_threads = disqus.get('threads.listPopular', forum=settings.DISQUS_FORUM_NAME, method='get')

    topic_list = []
    for popular_thread in popular_threads:
        try:
            title = popular_thread['clean_title_unescaped']
            topic = Topic.objects.get(title=title)
            topic_list.append(topic)
        except ObjectDoesNotExist:
            pass

    context = {
        'topic_list': topic_list,
    }

    return render(request, 'Topics/trending.html', context)


def all_topics(request):
    topic_list = Topic.objects.all()
    paginator = Paginator(topic_list, 20)

    page = request.GET.get('page')

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    context = {
        'topic_list': topics,
    }

    return render(request, 'Topics/all.html', context)


def search_topics(request):
    raw_topic_list = Topic.objects.raw("SELECT * "
                                       "FROM topics_topic "
                                       "WHERE title LIKE %s "
                                       "OR description LIKE %s",
                                       [
                                           '%%%s%%' % request.GET.get('search_query'),
                                           '%%%s%%' % request.GET.get('search_query'),
                                       ])
    topic_list = list(raw_topic_list)
    print(raw_topic_list.query)
    paginator = Paginator(topic_list, 20)

    page = request.GET.get('page')

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    context = {
        'topic_list': topics,
    }

    return render(request, 'Topics/all.html', context)


def view_topic(request, slug):
    try:
        topic = Topic.objects.get(slug=slug)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, _('Topic not found'))

        return HttpResponseRedirect(reverse('Topics:index'))

    StaticFile.js_files.append('comment_reply.js')

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