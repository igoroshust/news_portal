from django import template

register = template.Library()

BAN_WORDS = [
    'выведена',
    'предками',
    'первые',
    'выведен',
]

@register.filter()
def censor(value):
    for item in BAN_WORDS:
        value = value.replace(item[1:], f'{'*' * (len(item)-1)}')
    return value


