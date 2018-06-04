# coding:utf-8
from apps import db


# 定义任务模型
class Todo(db.Model):
    # 表名
    __tablename__ = 'todo'

    # 字段
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(120), unique=True)
    finished = db.Column(db.Boolean)

    def __repr__(self):
        return 'Todo:%s' % self.info


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
