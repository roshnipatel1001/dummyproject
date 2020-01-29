import datetime

from ..models import College, Student
import factory.fuzzy


class CollegeFactory(factory.Factory):
    """
        Define college Factory
    """

    class Meta:
        model = College
    clg_name = factory.fuzzy.FuzzyText(length=12, )
    city = factory.fuzzy.FuzzyText(length=12, )
    state = factory.fuzzy.FuzzyText(length=12, )


class StudentFactory(factory.Factory):
    """
        Define student Factory
    """

    class Meta:
        model = Student

    college_name = factory.SubFactory(CollegeFactory)
    branch = factory.fuzzy.FuzzyText(length=12, )
    address = factory.fuzzy.FuzzyText(length=12, )
    date_of_birth = factory.fuzzy.FuzzyDate(start_date=datetime.date(1, 1, 1)),
    first_name = factory.fuzzy.FuzzyText(length=12, )
    last_name = factory.fuzzy.FuzzyText(length=12, )
    email = factory.fuzzy.FuzzyText(length=12, )
    username = factory.fuzzy.FuzzyText(length=12, )
    password = factory.fuzzy.FuzzyText(length=12, )
