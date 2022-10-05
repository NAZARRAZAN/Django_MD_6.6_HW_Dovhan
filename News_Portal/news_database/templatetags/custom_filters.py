from django import template
from .sources import cleaning_word, returning_symbols_word
register = template.Library()


# sandman, have, united, pypi
@register.filter()
def censor(sentence):
    sentence = sentence.split(" ")
    result = ""
    ban_word_list = ["have", "sandman", "united", "pypi"]
    for word in sentence:
        if cleaning_word(word).lower() in ban_word_list:
            censured_word = cleaning_word(word).replace(f"{cleaning_word(word)[1:]}", "*" * (len(cleaning_word(word)) - 1))
            censured_word = list(censured_word)
            for symbol, index in returning_symbols_word(word).items():
                censured_word.insert(symbol, index)
            result += "".join(censured_word) + " "
        else:
            result += f"{word} "

    return result