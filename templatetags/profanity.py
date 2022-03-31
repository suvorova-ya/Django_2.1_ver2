from django import template
import os


register = template.Library()



@register.filter()
def censor(value):
    bad_words = ['Яндекс',',банки','Новости','Telegram']
    for word in bad_words:
        value = value.replace(word[1:], '*' * (len(word) - 1))
        return value








