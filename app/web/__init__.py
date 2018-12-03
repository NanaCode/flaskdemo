# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/1 18:10'

from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book  # 注意，和上面代码顺序不能调换
from app.web import user





