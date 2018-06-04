# -*- coding:utf8 -*-
from imp import reload

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()



import sys

reload(sys)
sys.setdefaultencoding("utf8")

app = Flask(__name__)

# 数据库配置：数据库地址/关闭自动跟踪修改
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/todolist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'itheima'

# 创建数据库对象
db = SQLAlchemy(app)

import apps.views



