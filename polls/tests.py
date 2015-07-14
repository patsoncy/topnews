from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from .models import Question
import datetime



# What happened is this:
# python manage.py test polls looked for tests in the polls application
# it found a subclass of the django.test.TestCase class
# it created a special database for the purpose of testing
# it looked for test methods - ones whose names begin with test
# in test_was_published_recently_with_future_question it created a Question instance whose pub_date field is 30 days
# in the future and using the assertEqual() method, it discovered that its was_published_recently() returns True,
# though we wanted it to return False
# The test informs us which test failed and even the line on which the failure occurred.

class QuestionMethodTest(TestCase):
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


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_np_questions(self):
        """如果没有问题，显示适当的提示"""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['last_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context['last_question_list'], ['<Question: Past question.>'])
