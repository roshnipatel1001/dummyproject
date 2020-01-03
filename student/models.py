from django.contrib.auth.models import AbstractUser
from django.db import models


class College(models.Model):
    clg_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.clg_name

    class Meta:
        db_table = "College"


class Student(AbstractUser):
    college_name = models.ForeignKey(
        College, related_name="college_student", on_delete=models.CASCADE, null=True
    )
    branch = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(max_length=100, null=True)

    class Meta:
        db_table = "Student"


