from django import template
import re
import pygments
from pygments.lexers import LEXERS, get_lexer_by_name
from pygments import highlight
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.filter(name='pygmentize')
def pygmentize(value):
    try:
        lexer = pygments.lexers.guess_lexer(value)
    except ValueError:
        lexer = pygments.lexers.PythonLexer()
    try:
        formatter = pygments.formatters.HtmlFormatter()
        hlvalue = pygments.highlight(value, lexer, formatter)
    except:
        hlvalue = "<pre>"+value+"</pre>"

    return hlvalue
