from django.db.models import signals
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student, College


# pre_save method signal
@receiver(signals.pre_save, sender=Student)
def check_college_name(sender, instance, **kwargs):
        student_data = Student.objects.all()
        clg_obj = College.objects.get(clg_name=student_data.get("college_name"))
        college_name=clg_obj
        for college_data in College.objects.all().values("clg_name"):
            if instance.clg_name == college_data:
             signals.pre_save.connect(check_college_name, sender=Student)`

            else:

                  # post_save method
                   @receiver(signals.post_save, sender=Student)
                   def create_Student(sender, instance, created, **kwargs):
                          print("Save method is called")
                     signals.post_save.connect(receiver=create_Student, sender=Student)

# # post_save method
# @receiver(signals.post_save, sender=Student)
# def create_Student(sender, instance, created, **kwargs):
#     print("Save method is called")


# def get(self, request, pk=None):
#     student = Student.objects.all()
#     for student_data in student:
#
#         clg_obj = College.objects.get(clg_name=student.get("college_name"))
#         college_name = clg_obj,
#         college_name = student_data.college_name
#         if college_name:
#             pass
#         else:
#             def create_student(sender, instance, created, **kwargs):
#                 print("Save is called")
#                 signals.post_save.connect(receiver=create_student, sender=Student)






