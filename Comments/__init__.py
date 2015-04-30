from .models import TopicComment
from .forms import TopicCommentForm


def get_model():
    return TopicComment


def get_form():
    return TopicCommentForm


def set_form_user(user):
    TopicCommentForm.user = user