# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/26 7:25'

from flask import jsonify, request
from helper import is_key_or_isbn
from yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字 isbn
    :param page: start count 缩减而来
    :return:
    """
    q = request.args['q']
    page = request.args['page']
    key_or_isbn = is_key_or_isbn(q)
    if key_or_isbn == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
