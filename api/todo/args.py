from webargs import fields, validate

todo_args = {
    # Required arguments and validations
    'name': fields.Str(required=True, validate=validate.Length(3)),
    'day': fields.Str(required=True, validate=validate.Length(3)),
    'description':fields.Str()
}

todo_id_arg = {
    'id': fields.Int()
}
