import random
import string


DOMAINS = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com", "yopemail.com"]
LETTERS = string.ascii_lowercase[:15]


def make_ramdom_email():
    return ''.join(random.choice(LETTERS) for i in range(8)) + '@' + random.choice(DOMAINS)
