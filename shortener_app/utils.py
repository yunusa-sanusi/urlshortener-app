import random
import string


def get_short_url(site):
    short_url = f'{site}/'
    size = 7
    letters = string.ascii_letters + string.digits
    letter_combination = ''.join(random.choices(letters, k=size))
    short_url += letter_combination
    return short_url
