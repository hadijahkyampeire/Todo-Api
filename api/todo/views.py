
from flask import request, jsonify, make_response
from flask_restful import Resource
from webargs.flaskparser import use_args
from .args import todo_args
from .args import todo_id_arg
from .models import Todo

class TodoListView(Resource):
    """Todolist class"""
    @use_args(todo_args, locations=('json', 'form'))
    def post(self, args):
        new_todo = Todo(
            name=args['name'],
            description=args['description'],
            day=args['day']
        )
        new_todo.save()
        response = {
            'messages': {
                'todo': [
                    'Todo successfully created'
                ]
            }
        }
        return make_response(jsonify(response), 201)

    def get(self):
        todos = Todo.query.all()
        items = []
        for todo in todos:
            todo_data = {}
            todo_data['id'] = todo.id
            todo_data['name'] = todo.name
            todo_data['description'] = todo.description
            todo_data['date_created'] = todo.date_created
            todo_data['day'] = todo.day
            todo_data['done'] = todo.done
            items.append(todo_data)
        
        response = {
            'messages': {
                'todo_items': [ 
                    items
                ]
            }
        }
        return make_response(jsonify(response), 200)


class TodoDetailView(Resource):
    @use_args(todo_id_arg, locations=('querystring', 'form'))
    def get(self, args):
        todo = Todo.query.filter_by(id=args['id']).first()
        if not todo:
            return make_response(jsonify({"message": {
                                'todo_item': "No item found by id"}
                            }), 404)
        response = {
            'messages': {
                'todo_item': {
                    'id': todo.id,
                    'name': todo.name,
                    'description': todo.description,
                    'day': todo.day,
                    'done': todo.done
                }
            }
        }
        return make_response(jsonify(response), 200)



    @use_args(todo_id_arg, locations=('querystring', 'form'))
    def delete(self, args):
        item = Todo.query.filter_by(id=args['id']).first()
        if not item:
            return make_response(jsonify({"message": {
                                'todo_item': "No item found by id"}
                            }), 404)
        item.delete()
        response = {
            'messages': {
                'todo': [
                    'Todo successfully deleted'
                ]
            }
        }
        return make_response(jsonify(response), 204)
    

    @use_args(todo_args, todo_id_arg, locations=('json','querystring', 'form'))
    def put(self, args):
        print(args)
        item = Todo.query.filter_by(id=args['id']).first()
        if not item:
            return make_response(jsonify({"message": {
                                'todo_item': "No item found by id"}
                            }), 404)
        item.name = args['name']
        item.description = args['description']
        item.day = args['day']
        item.save()
        response = {
            'messages': {
                'todo_item': {
                    'id': item.id,
                    'name': item.name,
                    'description': item.description,
                    'day': item.day,
                    'done': item.done
                }
            }
        }
        return make_response(jsonify(response), 200)

