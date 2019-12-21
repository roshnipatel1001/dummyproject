from service_objects.services import Service
from sqlparse.tokens import String

from .serializers import *


class CreateCollegeService(Service):
    def process(self):
        all_data = self.data.get("data")
        clg_obj = College.objects.create(clg_name=all_data.get("clg_name"),
                                         city=all_data.get("city"),
                                         state=all_data.get("state")
                                         )
        return clg_obj


class GetCollegeService(Service):
    def process(self):
        pk = self.data.get('pk')
        if pk:
            clg_get = College.objects.get(id=pk)
        else:
            clg_get = College.objects.all()
        return clg_get


class DeleteCollegeService(Service):
    def process(self):
        pk = self.data.get('pk')
        Clg_dlt = College.objects.get(pk=pk)
        Clg_dlt.delete()


class PutCollegeService(Service):
    def process(self):
        all_data = self.data.get("data")
        pk = all_data.get('id')
        college_new = College.objects.get(pk=pk)
        name = all_data.get('clg_name')
        city = all_data.get('city')
        state = all_data.get('state')

        college_new.clg_name = name
        college_new.city = city
        college_new.state = state
        college_new.save()

        return college_new


class CreateStudentService(Service):
    def process(self):
        student_data = self.data.get("data")
        clg_obj = College.objects.get(id=student_data.get("college_name"))
        student_obj = Student.objects.create(
            college_name=clg_obj,
            first_name=student_data.get("first_name"),
            last_name=student_data.get("last_name"),
            branch=student_data.get("branch"),
            date_of_birth=student_data.get("date_of_birth"),
            username=student_data.get("username"),
            # password=student_data.get("password"),
            email=student_data.get("email"),
            address=student_data.get("address"),
            last_login=student_data.get("last_login"),

        )
        student_obj.set_password("password")
        student_obj.save()
        return student_obj


class GetStudentService(Service):
    def process(self):
        pk = self.data.get('pk')
        if pk:

            student_get = Student.objects.get(id=pk)
        else:
            student_get = Student.objects.all()
        return student_get


class DeleteStudentService(Service):
    def process(self):
        pk = self.data.get('pk')
        student_dlt = Student.objects.get(pk=pk)
        student_dlt.delete()


class PutStudentService(Service):
    def process(self):
        all_data = self.data.get("data")
        pk = all_data.get('id')
        student_new = Student.objects.get(id=pk)
        fname = all_data.get("first_name")
        lname = all_data.get("last_name")
        branch = all_data.get("branch")
        DOB = all_data.get("date_of_birth")
        uname = all_data.get("username")
        password = all_data.get("password")
        address = all_data.get("address")
        email = all_data.get("email")
        last_login = all_data.get("last_login")

        student_new.first_name = fname
        student_new.last_name = lname
        student_new.branch = branch
        student_new.date_of_birth = DOB
        student_new.username = uname
        student_new.password = password
        student_new.address = address
        student_new.email = email
        student_new.last_login = last_login

        student_new.college_name = College.objects.get(id=2)
        student_new.save()
        return student_new
