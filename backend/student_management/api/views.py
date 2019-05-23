from flask import current_app as app

from flask_restful import Resource
from .utils import return_response


class StatusView(Resource):
    def get(self):
        app.logger.info("status check")
        return return_response({"status": "OK"}, 200)


class StudentListView(Resource):
    def get(self):
        pass


class StudentDetailView(Resource):
    def get(self, student_id):
        pass
