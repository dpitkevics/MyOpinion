from django import template

from MyOpinion.settings import STATIC_URL

register = template.Library()


class StaticFile(template.Node):
    css_files = []
    js_files = []

    def __init__(self, render_type):
        self.render_type = render_type

    @staticmethod
    def make_css_tag(css_file):
        return '<link rel="stylesheet" type="text/css" href="%scss/%s" />' % (STATIC_URL, css_file)

    @staticmethod
    def make_js_tag(js_file):
        return '<script src="%sjs/%s"></script>' % (STATIC_URL, js_file)

    def render(self, context):
        static_file_string = ''

        if self.render_type == 'css':
            for css_file in self.css_files:
                static_file_string += self.make_css_tag(css_file)
        elif self.render_type == 'js':
            for js_file in self.js_files:
                static_file_string += self.make_js_tag(js_file)

        return static_file_string


@register.tag(name='render_css_files')
def render_css_files(parser, value):
    return StaticFile('css')


@register.tag(name='render_js_files')
def render_css_files(parser, value):
    return StaticFile('js')