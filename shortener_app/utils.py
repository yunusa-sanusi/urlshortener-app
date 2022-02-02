import random
import string


def get_short_url():
    token = ''
    size = 7
    letters = string.ascii_letters + string.digits
    letter_combination = ''.join(random.choices(letters, k=size))
    token += letter_combination
    return token
