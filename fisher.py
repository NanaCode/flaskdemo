# _*_ coding: utf-8 _*_
from yushu_book import YuShuBook

__author__ = 'Nana'
__date__ = '2018/11/20 11:43'

import json
from flask import Flask, make_response
from helper import is_key_or_isbn

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 isbn
    :param page: start count 缩减而来
    :return:
    """
    key_or_isbn = is_key_or_isbn(q)
    if key_or_isbn == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # return json.dumps(result)  # 纯文本
    return json.dumps(result), 200, {"content-type": "application/json"}  # 格式化


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
