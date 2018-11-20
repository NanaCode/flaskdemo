# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/20 11:43'

from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 isbn
    :param page: start count 缩减而来
    :return:
    """
    # isbn13 13个0-9的数字组成
    # isbn10 10个0到9的数字组成，含有一些‘-’
    is_key_or_isbn = 'key'
    if len(q) == 13 and q.isdigit():
        is_key_or_isbn = 'isbn'
    short_q = q.replace('-', '')
    if '-' in short_q and len(short_q) == 10 and short_q.isdigit():
        is_key_or_isbn = 'isbn'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
