from django import forms
from django_comments import forms as comment_forms
from .models import TopicComment


class TopicCommentForm(comment_forms.CommentForm):
    user = None

    def __init__(self, *args, **kwargs):
        super(TopicCommentForm, self).__init__(*args, **kwargs)

        if self.user and self.user.is_authenticated():
            self.fields['email'] = forms.CharField(widget=forms.HiddenInput(), initial=self.user.email)
            self.fields['name'] = forms.CharField(widget=forms.HiddenInput(), initial=self.user.username)

        self.fields['url'] = forms.CharField(widget=forms.HiddenInput(), initial='http://jooglin.com')

    class Meta:
        model = TopicComment
