def cleaning_word(word):
    my_check_list = [":", ",", ".", ")", "(", "?", "!"]
    for check in my_check_list:
        if check in word:
            return cleaning_word(word.replace(f"{check}", ""))

    return word

def returning_symbols_word(word):
    my_check_list = [":", ",", ".", ")", "(", "?", "!"]
    my_simbols_dict = {}
    for check in my_check_list:
        if check in word:
            my_simbols_dict.update({word.index(f"{check}"): check})

    return my_simbols_dict

