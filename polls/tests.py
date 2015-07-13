from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question

# What happened is this:
# python manage.py test polls looked for tests in the polls application
# it found a subclass of the django.test.TestCase class
# it created a special database for the purpose of testing
# it looked for test methods - ones whose names begin with test
# in test_was_published_recently_with_future_question it created a Question instance whose pub_date field is 30 days in the future
# ... and using the assertEqual() method, it discovered that its was_published_recently() returns True, though we wanted it to return False
# The test informs us which test failed and even the line on which the failure occurred.

class QustionMethodTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)
