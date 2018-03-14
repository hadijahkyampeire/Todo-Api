
from flask import request, jsonify, make_response
from flask_restful import Resource
from webargs.flaskparser import use_args
from .args import todo_args
from .models import Todo

class TodoListView(Resource):
    """Todolist class"""
    @use_args(todo_args, locations=('json', 'form'))
    def post(self, args):
        print(args)
