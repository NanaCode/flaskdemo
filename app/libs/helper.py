# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/20 15:07'


def is_key_or_isbn(key_word):
    """
    :param q: 普通关键字 isbn
    :return:
    """
    # isbn13 13个0-9的数字组成
    # isbn10 10个0到9的数字组成，含有一些‘-’
    key_or_isbn = 'key'
    if len(key_word) == 13 and key_word.isdigit():
        key_or_isbn = 'isbn'
    short_q = key_word.replace('-', '')
    if '-' in short_q and len(short_q) == 10 and short_q.isdigit():
        key_or_isbn = 'isbn'
    return key_or_isbn
