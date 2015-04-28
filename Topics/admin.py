from django.contrib import admin

from MyOpinion.settings import APP_NAME
from .models import Topic, TopicTag, TopicCategory

admin.site.site_header = APP_NAME
admin.site.site_title = APP_NAME


class TopicTagInline(admin.TabularInline):
    model = TopicTag.topics.through


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        TopicTagInline
    ]

admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicTag)
admin.site.register(TopicCategory)
