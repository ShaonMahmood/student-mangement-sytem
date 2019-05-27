from marshmallow import Schema, fields


class StudentSchema(Schema):
    student_id = fields.Str()
    roll = fields.Int()
    name = fields.Str()
    student_class = fields.Int()
    date_of_birth = fields.Date()
    address = fields.Str()
    phone_number = fields.Str()
    email_address = fields.Email()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class StudentUpdateSchema(Schema):
    roll = fields.Int()
    name = fields.Str()
    student_class = fields.Int()
    address = fields.Str()
    phone_number = fields.Str()
    email_address = fields.Email()

