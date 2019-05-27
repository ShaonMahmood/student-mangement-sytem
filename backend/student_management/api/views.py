from flask import current_app as app, request

from flask_restful import Resource
from marshmallow import ValidationError
from google.appengine.ext import ndb

from .utils import return_response
from .models import Student
from .serializers import StudentSchema, StudentUpdateSchema


class StatusView(Resource):
    def get(self):
        app.logger.info("status check")
        return return_response({"status": "OK"}, 200)


class StudentListView(Resource):
    def get(self):
        qry = Student.query().order(-Student.created_at)
        students = qry.fetch(10)
        result, errors = StudentSchema(many=True).dump(students)
        if errors:
            response = return_response(errors, 404)
        else:
            response = return_response(result, 200)
        return response

    def post(self):
        json_data = request.get_json()

        data, errors = StudentSchema().load(json_data)

        if errors:
            return return_response(errors, 400)

        try:
            issue = Student(**data).put()
        except Exception as e:
            error_message = {"error": str(e)}
            return return_response(error_message, 400)

        result, errors = StudentSchema().dump(issue)
        return return_response(result, 201)


class StudentDetailView(Resource):
    def get(self, student_id):

        try:
            student_entity = ndb.Key(Student, str(student_id)).get()
        except Exception as e:
            error_message = {"error": str(e)}
            return return_response(error_message, 404)

        result, errors = StudentSchema().dump(student_entity)
        if errors:
            response = return_response(errors, 404)
        else:
            response = return_response(result, 200)
        return response

    def put(self, student_id):

        json_data = request.get_json()
        data, errors = StudentUpdateSchema().load(json_data)
        if errors:
            return return_response(errors, 400)

        try:
            student_entity = ndb.Key(Student, str(student_id)).get()
        except Exception as e:
            error_message = {"error": str(e)}
            return return_response(error_message, 404)

        student_entity.populate(**data)
        student_entity.put()
        result, errors = StudentSchema().dump(student_entity)
        return return_response(result, 200)

    def delete(self, student_id):
        try:
            student_entity = ndb.Key(Student, str(student_id)).get()
        except Exception as e:
            error_message = {"error": str(e)}
            return return_response(error_message, 404)

        student_entity.key.delete()
        message = {"success": "id with {0} is deleted".format(student_id)}
        return return_response(message, 200)
