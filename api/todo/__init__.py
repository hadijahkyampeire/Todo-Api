from flask import Blueprint
from flask_restful import Api
from api.todo.views import TodoListView, TodoDetailView

todo = Blueprint('todo', __name__, url_prefix='/todo')
todo_api = Api(todo)

todo_api.add_resource(TodoListView, '/todos')
todo_api.add_resource(TodoDetailView, '/todos/<int:todo_id>')

