'''
Created on Sep 23, 2016

@author: rtorres
'''


def split_name(name):
    name = name.strip()
    pivot = name.rfind(' ')
    if pivot > 0:
        first_name = name[:pivot]
        last_name = name[pivot + 1:]
    else:
        first_name = name
        last_name = ''
    return first_name, last_name
