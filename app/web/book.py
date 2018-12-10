# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/26 7:25'

from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_key_or_isbn
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字 isbn
    :param page: start count 缩减而来
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        key_or_isbn = is_key_or_isbn(q)
        if key_or_isbn == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
