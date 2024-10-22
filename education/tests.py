from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from education.models import Lesson, Subscriptions, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='alexey@mail.ru')
        self.course = Course.objects.create(course_name='философия')
        self.lesson = Lesson.objects.create(lesson_name= 'русский язык', owner=self.user, course=self.course)
        self.subscriptions = Subscriptions.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)


    def test_lesson_retrive(self):
        url = reverse("education:lesson-detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('lesson_name'), self.lesson.lesson_name
        )
        self.assertEqual(
            data.get('course'), self.course.pk
        )

    def test_lesson_create(self):
        url = reverse("education:lesson-create")
        data = {
            "lesson_name": "история",
            "course": self.course.pk,
            "owner": self.user.pk,
            "lesson_link": 'youtube.com'
        }

        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(), 2
        )
    def test_lesson_update(self):
        url = reverse("education:lesson-update", args=(self.lesson.pk,))
        data = {
            "lesson_name": "история",
            "course": self.course.pk,
            "owner": self.user.pk,
            "lesson_link": '414youtube.com'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('lesson_name'), "история"
        )
        self.assertEqual(
            data.get("lesson_link"), '414youtube.com'
        )

    def test_lesson_delete(self):
        url = reverse("education:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("education:lesson-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "lesson_link": None,
                    "lesson_name": self.lesson.lesson_name,
                    "lesson_discription": None,
                    "lesson_image": None,
                    "course": self.course.pk,
                    "owner": self.user.pk

                }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

class SubscriptionsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='alexey@mail.ru')
        self.course = Course.objects.create(course_name='философия')
        self.client.force_authenticate(user=self.user)


    def test_subscription_activate(self):
        url = reverse("education:subscriptions-create")
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }

        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "message": "подписка добавлена",
            },
        )
        self.assertTrue(
            Subscriptions.objects.all().exists(),
        )

    def test_subscription_list(self):
        self.subscriptions = Subscriptions.objects.create(user=self.user, course=self.course)
        url = reverse("education:subscriptions-list")
        response = self.client.get(url)
        data = response.json()
        result = [{
            "id": self.subscriptions.pk,
            "is_sub": False,
            "user": self.user.pk,
            "course": self.course.pk
        }]
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


    def test_subscription_deactivate(self):
        Subscriptions.objects.create(user=self.user, course=self.course)
        url = reverse("education:subscriptions-create")
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.json(),
            {
                "message": "подписка удалена",
            },
        )
        self.assertFalse(
            Subscriptions.objects.all().exists(),
        )