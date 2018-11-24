# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/22 23:12'
from http import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def search_by_isbn(self, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    def search_by_keyword(self, keyword):
        url = YuShuBook.isbn_url.format(keyword)
        result = HTTP.get(url)
        return result