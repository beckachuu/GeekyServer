import string
import random


def random_string(length=None):
    if length is None:
        length = random.randint(5, 20)

    return str(''.join(random.choices(string.ascii_uppercase + string.digits, k=length)))
