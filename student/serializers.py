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


class CollegeSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = College
        fields = ['id', 'clg_name', 'city', 'state', 'college_student']
