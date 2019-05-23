from student_management.api import api
from .views import (
    StatusView,
    StudentListView,
    StudentDetailView
)

api.add_resource(StudentListView, '/students')
api.add_resource(StudentDetailView, '/students/<student_id>')
api.add_resource(StatusView, '/status')
