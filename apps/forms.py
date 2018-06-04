# coding:utf-8

# 自定义表单类
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    todo = StringField('todo', validators=[DataRequired()])
    submit = SubmitField('submit')