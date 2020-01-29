from rest_framework import status
from rest_framework.test import APITestCase
from ..models import College, Student


class CollegeTests(APITestCase):
    def test_create_clg(self):
        """
        Ensure we can create a new college object.
        """
        url = '/clg/'
        data = {'clg_name': 'sait', 'city': 'indore', 'state': 'mp', 'college_student': '1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # def test_get_clg(self):
        """
        Ensure we can get a college objects.
        """
        # url = '/clg/'
        response1 = self.client.get(url)

        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    # def test_put(self):
    #     """PUT to update a college."""
    #     college = CollegeFactory()
    #     data = {
    #         'clg_name': 'bansal ',
    #         'city': 'bhopal ',
    #         'state': 'mp ',
    #
    #     }
    #     url = '/clg/1/'
    #     breakpoint()
    #
    #     response = self.client.put(url(college.id), data=data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class StudentTests(APITestCase):
    def setUp(self):
        self.college = College.objects.create(clg_name='sait', city='indore', state='mp')
        college=self.college
        self.student = Student.objects.create(college_name=college, branch='cs', address='sanawad',
                                              date_of_birth='1998-01-10', first_name='roshni', last_name='patel',
                                              username='admin123')

    def test_create_student(self):
        """
        Ensure we can create a new student object.
        """

        url = '/student/'
        breakpoint()

        response = self.client.post(url, self.student)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # def test_get_clg(self):
        """
        Ensure we can get a student objects.
        """
        # url = '/clg/'
        response1 = self.client.get(url)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
