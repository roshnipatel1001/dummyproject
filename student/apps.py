# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class StudentConfig(AppConfig):
    name = 'student'

    def ready(self):
        import student.signals
