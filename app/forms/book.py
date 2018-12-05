# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/4 22:40'

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])  # 数组，可以传入多个验证对象
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
