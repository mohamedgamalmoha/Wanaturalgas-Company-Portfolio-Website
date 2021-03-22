from django import template
from bs4 import BeautifulSoup

register = template.Library()


@register.filter(name='str_split')
def split_str(_str, num):
    if not str.isnumeric(num):
        raise ValueError("Not valid number")
    soup = BeautifulSoup(_str, "html.parser").text.lower()[:int(num)]
    return str(soup)
