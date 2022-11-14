import random
import string
import time


def random_string(length=None):
    if length is None:
        length = random.randint(5, 20)

    return str(''.join(random.choices(string.ascii_uppercase + string.digits, k=length)))


def get_current_datetime():
    return time.strftime('%Y-%m-%d %H:%M:%S')
