from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .services import (
    CreateCollegeService,
    GetCollegeService,
    DeleteCollegeService,
    PutCollegeService,
    CreateStudentService,
    GetStudentService,
    DeleteStudentService,
    PutStudentService,
)
from .tasks import send_email_task


class CollegeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        clg_serializer = CollegeSerializer(data=request.data)
        if clg_serializer.is_valid(raise_exception=True):
            CreateCollegeService.execute({"data": request.data})
            return Response(clg_serializer.data, status=201)
        return Response(clg_serializer.errors, status=400)

    def get(self, request, pk=None):
        clg_get = GetCollegeService.execute({"pk": pk})
        if pk:
            serializer = CollegeSerializer(clg_get)
        else:
            serializer = CollegeSerializer(clg_get, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        DeleteCollegeService.execute({"pk": pk})
        return Response(data={"message": "deleteted"}, status=200)

    def put(self, request, pk):
        clg_ut = College.objects.get(pk=pk)
        data = request.data
        clg_serializer = CollegeSerializer(clg_ut, data=request.data)
        if clg_serializer.is_valid(raise_exception=True):
            PutCollegeService.execute({"clg_ut": clg_ut, "data": request.data})
            return Response(clg_serializer.data, status=201)
        return Response(clg_serializer.errors, status=400)


class SendEmailView(APIView):
    def get(self, request, pk=None):
        student = Student.objects.all()
        for student_data in student:
            from_email = settings.EMAIL_HOST_USER
            to_email = student_data.email
            send_mail('Celery Task Worked!!!!!!!!',
                      'This is proof the task worked in users!', from_email, [to_email],
                      fail_silently=False, html_message='This is proof the task worked!')
        return Response(data={"Message": "success"}, status=200)


class StudentView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid(raise_exception=True):
            college_name = CreateStudentService.execute({"data": request.data})
            student_serializer = StudentSerializer(college_name)
            return Response(student_serializer.data, status=201)
        return Response(student_serializer.errors, status=400)

    def get(self, request, pk=None):
        student_get = GetStudentService.execute({"pk": pk})
        if pk:
            student_serializer = StudentSerializer(student_get)
        else:
            student_serializer = StudentSerializer(student_get, many=True)
        return Response(student_serializer.data)

    def delete(self, request, pk):
        DeleteStudentService.execute({"pk": pk})
        return Response(data={"message": "deleted"}, status=200)

    def put(self, request, pk):
        student_update = Student.objects.get(pk=pk)
        data = request.data
        student_serializer = StudentSerializer(student_update, data=request.data)
        if student_serializer.is_valid(raise_exception=True):
            PutStudentService.execute(
                {"student_update": student_update, "data": request.data}
            )
            return Response(student_serializer.data, status=201)
        return Response(student_serializer.errors, status=400)


def index(self):
    send_email_task.delay()
    return HttpResponse("all done")
