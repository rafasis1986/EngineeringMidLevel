'''
Created on Oct 16, 2016

@author: rtorres
'''
from flaskiwsapp.extensions import cache
from flaskiwsapp.snippets.constants import CACHE_KEY_PHONE, CACHE_KEY_USER
from flaskiwsapp.snippets.utils import generate_key
from flaskiwsapp.snippets.exceptions.cacheExceptions import CacheExpiredException
from flaskiwsapp.snippets.exceptions.userExceptions import UserBadKeyException


def save_client_phone_cache(user_id, phone):
    key = generate_key(6)
    cache.set(CACHE_KEY_USER % user_id, key)
    cache.set(CACHE_KEY_PHONE % user_id, phone)
    return key


def delete_client_phone_cache(user_id):
    cache.delete(CACHE_KEY_USER % user_id)
    cache.delete(CACHE_KEY_PHONE % user_id)


def get_client_phone_cache(user_id, key):
    key_saved = cache.get(CACHE_KEY_USER % user_id)
    if key_saved is None:
        raise CacheExpiredException(CACHE_KEY_USER % user_id)
    if key == key_saved:
        phone = cache.get(CACHE_KEY_PHONE % user_id)
        cache.delete(CACHE_KEY_USER % user_id)
    else:
        raise UserBadKeyException()
    return phone
