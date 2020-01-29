import unittest

from .factories import CollegeFactory, StudentFactory


class collegeTest(unittest.TestCase):

    def test_with_factory_boy(self):
        college = CollegeFactory(
            clg_name='sait',
            city='indore',
            state='mp',

        )
        self.assertEqual(college.clg_name, "sait")
        self.assertEqual(college.city, "indore")
        self.assertEqual(college.state, "mp")


class studentTest(unittest.TestCase):
    def test_with_factory_boy(self):
        clg_obj = CollegeFactory(clg_name='sait')

        student = StudentFactory(

            college_name=clg_obj,
            branch='cs',
            address='sanawad',
            date_of_birth='1998-01-10',
            first_name='roshni',
            last_name='patel',
            email='r@gmail.com',
            username='admin',
            password='admin123456',

        )
        self.assertEqual(student.college_name, clg_obj)
        self.assertEqual(student.branch, "cs")
        self.assertEqual(student.address, "sanawad")
        self.assertEqual(student.date_of_birth, "1998-01-10")
        self.assertEqual(student.first_name, "roshni")
        self.assertEqual(student.last_name, "patel")
        self.assertEqual(student.email, "r@gmail.com")
        self.assertEqual(student.username, "admin")
        self.assertTrue(student.password, "80684786")


from django.test import TestCase
from ..models import College


class CollegeTest(TestCase):

    def test_string_representation(self):
        college = College(clg_name="mp")
        self.assertEqual(str(college), college.clg_name)

