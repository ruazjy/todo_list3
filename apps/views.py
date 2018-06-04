# coding:utf-8
from flask import render_template, flash, url_for, redirect, request
from apps import app, db
from apps.models import Todo
from apps.forms import TodoForm


@app.route('/delete/<todo_id>')
def delete_todo(todo_id):
    # 查询数据库，如果有该任务，则删除。如果没有则提示错误
    todo = Todo.query.get(todo_id)
    if todo:
        try:
            db.session.delete(todo)
            db.session.commit()
        except Exception as e:
            print e
            flash('Delete mission failed.')
            db.session.rollback()
    else:
        flash('The mission not exists.')
    return redirect(url_for('index'))


@app.route('/finished/<todo_id>')
def done_todo(todo_id):
    # 查询数据库，是否该ID的书，如果有就删除，没有就提示错误
    todo = Todo.query.get(todo_id)
    if todo:
        try:
            todo.finished = True
            db.session.add(todo)
            db.session.commit()
        except Exception as e:
            flash('Change mission situation to finished failed.')
            db.session.rollback()
    else:
        flash('Can not find the book.')

    # 如何返回当前网址 --> 重定向
    # redirect:重定向，需要传入网络或者路由地址
    # url_for:需要传入视图函数名，返回该视图函数对应的路由地址
    return redirect(url_for('index'))


@app.route('/', methods=["GET", "POST"])
def index():
    # 创建自定义的表单类
    todo_form = TodoForm()

    '''
    验证逻辑：
    1.调用wtf的函数实现验证
    2.验证获取数据
    3.判断作者是否存在
    4.如果作者存在，判断书籍是否存在，没有重复书籍就添加数据，如果重复就提示错误
    5.如果作者不存在，添加作者和书籍
    6.验证不通过就提示错误
    '''
    if todo_form.validate_on_submit():
        # 2.验证获取数据
        todo_info = todo_form.todo.data
        todo_finished = False

        # 3.判断任务是否存在
        todo = Todo.query.filter_by(info=todo_info).first()

        # 4.如果任务存在，则提示错误；不存在，则添加任务
        if todo:
            flash('The mission already exists.')
        else:
            try:
                new_todo = Todo(info=todo_info, finished=todo_finished)
                db.session.add(new_todo)
                db.session.commit()
            except Exception as e:
                print e
                flash('Insert mission failed.')
                db.session.rollback()
    else:
        if request.method == 'POST':
            flash('information not completed')

    # 查询所有的任务信息，让信息传递给模板
    todos = Todo.query.all()
    return render_template('todo.html', todos=todos, form=todo_form)
