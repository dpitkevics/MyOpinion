from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TopicCategory(TimestampModel):
    title = models.CharField(max_length=258)
    slug = models.SlugField()

    class Meta:
        verbose_name = _('Topic Category')
        verbose_name_plural = _('Topic Categories')
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.slug = slugify(self.title)

        super(TopicCategory, self).save(force_insert, force_update, using, update_fields)


class Topic(TimestampModel):
    title = models.CharField(max_length=258)
    description = models.TextField()
    slug = models.SlugField()

    author = models.ForeignKey(User)
    category = models.ForeignKey(TopicCategory)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.slug = slugify(self.title)

        super(Topic, self).save(force_insert, force_update, using, update_fields)


class TopicTag(TimestampModel):
    topics = models.ManyToManyField(Topic, blank=True)
    title = models.CharField(max_length=64)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.slug = slugify(self.title)

        super(TopicTag, self).save(force_insert, force_update, using, update_fields)