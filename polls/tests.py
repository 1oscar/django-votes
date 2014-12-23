import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from polls.models import Question


def create_question(question_text, days):
    """
    Create a question with the given question_text published the given
    number of days offset to now (negative fo rquestions published in the past
    ,positive for questions that have yet to be published
    :param question_text:
    :param days:
    :return:
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_question(self):
        """
        if no question exist, an appropriate message should be displayed.
        """

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """Question with a pub_date in the should be displayed on the
        index page
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question:Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """Question with a pub_date in the future should not be displayed on
        the index page
        """

        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.",
                            statue_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exit,only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question:Past question.>'])

    def test_index_view_with_two_past_question(self):
        """
        Even if both past and future questions exit,only past questions
        should be displayed.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2 .", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question:Past question 2.>', '<Question:Past question 1.>']
        )


    # def test_was_published_recently_with_old_question(self):
    #     """
    #     was_published should return False for Questions whose
    #     pub_date is in the future
    #     """
    #
    #     time = timezone.now()-datetime.timedelta(days=30)
    #     old_question = Question(pub_date=time)
    #     self.assertEqual(old_question.was_published_recently(), False)
    #
    # def test_was_published_recently_with_recent_question(self):
    #     """
    #     was_published_recently() should return True for questions whose
    #     pub_date is within the latest day
    #     """
    #
    #     time = timezone.now() - datetime.timedelta(hours=1)
    #     recent_question = Question(pub_date=time)
    #     self.assertEqual(recent_question.was_published_recently(), True)


