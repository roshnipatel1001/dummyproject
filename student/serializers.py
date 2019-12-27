from rest_framework import serializers
from .models import *


class CollegeSerializer1(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        extra_kwargs = {
            "username": {"default": "username"},
            "password": {"default": "password", "write_only": "True"},
        }


class CollegeSerializer(serializers.ModelSerializer):
    college_student = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = College
        fields = ["id", "clg_name", "city", "state", "college_student"]


class EmailSerializer(serializers.ModelSerializer):
    message = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
