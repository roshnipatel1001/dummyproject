from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import College


class CollegeTests(APITestCase):
    def test_create_college(self):
        """
        Ensure we can create a new match object.
        """
        url = '/clg/'
        data = {
                    "clg_name": "sdfg",
                    "city": "indore",
                    "state": "mp",
                    "college_student": [
                        {
                            "id": 3,
                            "college_name": "sims",
                            "last_login": "2019-12-26T08:14:19Z",
                            "is_superuser": "false",
                            "username": "roshni123",
                            "first_name": "Roshni",
                            "last_name": "Patel",
                            "email": "r@gmail.com",
                            "is_staff": "false",
                            "is_active": "true",
                            "date_joined": "2019-12-26T10:28:34.742358Z",
                            "branch": "cs",
                            "date_of_birth": "2019-12-26",
                            "address": "edf",
                            "groups": [],
                            "user_permissions": []
                        }
                    ]
        }
        response = self.client.post(url, data, format='json')
        breakpoint()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
