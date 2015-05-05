from django.template import Library
from django.core.urlresolvers import reverse
from django.core.cache import get_cache

import time
from datetime import datetime

from Disqus import DisqusAPI, APIError

from MyOpinion import settings


register = Library()
cache = get_cache('default')


@register.assignment_tag()
def get_comments(link):
    disqus = DisqusAPI(settings.DISQUS_SECRET_KEY, settings.DISQUS_PUBLIC_KEY)

    thread_query = 'link:%s' % link

    posts_list = disqus.get('threads.listPosts', forum=settings.DISQUS_FORUM_NAME, thread=thread_query, method='get')

    return posts_list


@register.assignment_tag()
def get_comment_count(link):
    key_format = 'disqus_comment_count_%s'
    comment_count = cache.get(key_format % link)
    if not comment_count:
        try:
            posts_list = get_comments(link)
            comment_count = len(posts_list)
        except APIError:
            comment_count = 0

        cache.set(key_format % link, comment_count, 300)

    return comment_count


@register.assignment_tag()
def get_forum_url(request, slug):
    full_url = 'http://%s%s' % (request.get_host(), reverse('Topics:view_opinion', kwargs={'slug': slug}))

    return full_url


@register.assignment_tag()
def get_latest_action(link):
    try:
        posts_list = get_comments(link)
    except APIError:
        return None

    try:
        latest_post = posts_list[0]
    except IndexError:
        return None

    time_struct = time.strptime(latest_post['createdAt'], '%Y-%m-%dT%H:%M:%S')
    dt = datetime.fromtimestamp(time.mktime(time_struct))

    return dt