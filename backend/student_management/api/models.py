from google.appengine.ext import ndb


class Student(ndb.Model):
    student_id = ndb.StringProperty()
    roll = ndb.IntegerProperty()
    name = ndb.StringProperty()
    student_class = ndb.IntegerProperty()
    date_of_birth = ndb.DateProperty()
    address = ndb.StringProperty()
    phone_number = ndb.StringProperty()
    email_address = ndb.StringProperty()
    created_at = ndb.DateTimeProperty(auto_now=True)
    updated_at = ndb.DateTimeProperty(auto_now_add=True)
