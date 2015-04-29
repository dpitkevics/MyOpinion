from django_comments.models import Comment
from .forms import TopicCommentForm


def get_model():
    return Comment


def get_form():
    return TopicCommentForm


def set_form_user(user):
    TopicCommentForm.user = user