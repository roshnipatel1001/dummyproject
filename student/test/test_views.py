from unittest import TestCase
from django.test import RequestFactory
from mock import patch, MagicMock
from .factories import CollegeFactory, StudentFactory
from ..views import CollegeView, College, StudentView, Student


@patch('student.models.College.save', MagicMock(name="save"))
class CollegeViewTest(TestCase):
    def setUp(self):
        self.college = CollegeFactory()
        self.factory = RequestFactory()

    def test_post(self):
        """
        Test post requests
        """
        # Create the request
        data = {
            'clg_name': 'dfghjk ',
            'city': 'sdfghjk',
            'state': 'xcvbnm',

        }
        request = self.factory.post(('/clg/'), data)

        request.data = self.college

        # Get the response
        response = CollegeView.as_view()(request)
        self.assertEqual(response.status_code, 201)
        # Check save was called
        self.assertTrue(College.save.called)
        self.assertEqual(College.save.call_count, 1)


@patch('student.models.Student.save', MagicMock(name="save"))
class StudentViewTest(TestCase):
    def setUp(self):
        self.student = StudentFactory()
        self.factory = RequestFactory()

    def test_post(self):
        """
        Test post requests
        """
        clg_obj = CollegeFactory(clg_name='astral')
        # Create the request
        data = {
            'college_name': clg_obj,
            'branch': 'dfghjk ',
            'address': 'sanawad',

        }

        request = self.factory.post(('/student/'), data)
        request.data = self.student
        # Get the response
        response = StudentView.as_view()(request)

        self.assertEqual(response.status_code, 201)
        # Check save was called
        self.assertTrue(Student.save.called)
        self.assertEqual(Student.save.call_count, 1)


class CollegeGetTest(TestCase):
    """
    Test the snippet create view
    """

    def setUp(self):
        self.college = CollegeFactory()
        self.factory = RequestFactory()

    def test_get_all(self):
        """
        Test GET requests
        """
        request = self.factory.get('/clg/')
        request.college = self.college
        response = CollegeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    # def test_get_by_id(self):
    #     """
    #     Test GET requests
    #     """
    #     # college = CollegeFactory(id=1)
    #     pk=self.get('pk')
    #     college = College.objects.get(id=pk)
    #
    #     request = self.factory.get('/clg/13/')
    #     # request= self.is_(kwargs={'pk': college.pk})
    #
    #     request.college = self.college
    #     response = CollegeView.as_view()(request)
    #     self.assertEqual(response.status_code, 200)


class StudentGetTest(TestCase):
    """
    Test the snippet create view
    """

    def setUp(self):
        self.student = StudentFactory()
        self.factory = RequestFactory()

    def test_get_all(self):
        """
        Test GET requests
        """
        request = self.factory.get('/student/')
        request.student = self.student
        response = StudentView.as_view()(request)
        self.assertEqual(response.status_code, 200)
