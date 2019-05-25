from flask import current_app as app, request

from flask_restful import Resource
from marshmallow import ValidationError

from .utils import return_response
from .models import Student
from .serializers import StudentSchema, StudentUpdateSchema

class StatusView(Resource):
    def get(self):
        app.logger.info("status check")
        return return_response({"status": "OK"}, 200)


class StudentListView(Resource):
    def get(self):
        categories = Student.objects
        result, errors = StudentSchema(many=True).dump(categories)
        if errors:
            response = return_response(errors, 404)
        else:
            response = return_response(result, 200)
        return response
        pass

    def post(self):
        json_data = request.get_json()

        data, errors = StudentSchema().load(json_data)

        if errors:
            return return_response(errors, 400)

        try:
            issue = Student(**data).save()
        except ValidationError as e:
            error_message = {"error": str(e)}
            return return_response(error_message, 400)

        result, errors = StudentSchema().dump(issue)
        return return_response(result, 201)

        pass


class StudentDetailView(Resource):
    def get(self, student_id):

        try:
            worker_issue = Student.objects(id=student_id).get()
        except Student.DoesNotExist:
            error_message = {
                "error": "WorkerIssue Object Not Found"
            }
            return return_response(error_message, 404)
        result, errors = StudentSchema().dump(worker_issue)
        if errors:
            response = return_response(errors, 404)
        else:
            response = return_response(result, 200)
        return response
        pass
    def put(self, student_id):

        json_data = request.get_json()
        data, errors = StudentUpdateSchema().load(json_data)
        if errors:
            return return_response(errors, 400)

        try:
            worker_issue = Student.objects(id=student_id).get()
        except Student.DoesNotExist:
            error_message = {
                "error": "WorkerIssue Object Not Found"
            }
            return return_response(error_message, 404)

        worker_issue.status = data.get("status", worker_issue.status)
        worker_issue.worker_feedback = data.get("worker_feedback", worker_issue.worker_feedback)
        worker_issue.save()
        result, errors = StudentSchema().dump(worker_issue)
        return return_response(result, 200)
        pass
    def delete(self, student_id):
        pass
