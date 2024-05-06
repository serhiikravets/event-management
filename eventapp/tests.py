from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from eventapp.models import Event

User = get_user_model()


class EventViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.event = Event.objects.create(title='Test Event', description='Test Description', location='Test Location', date='2022-12-31', organizer=self.user)
        self.client.force_authenticate(user=self.user)

    def test_list_events(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event(self):
        response = self.client.post('/events/', {
            'title': 'New Event',
            'description': 'New Description',
            'location': 'New Location',
            'date': '2022-12-31',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_event(self):
        response = self.client.get(f'/events/{self.event.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_event(self):
        response = self.client.put(f'/events/{self.event.pk}/', {'title': 'Updated Event', 'description': 'Updated Description', 'location': 'Updated Location', 'date': '2022-12-31'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_event(self):
        response = self.client.delete(f'/events/{self.event.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_register_event(self):
        response = self.client.post(f'/events/{self.event.pk}/register/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.event.attendees.count(), 1)

    def test_unregister_event(self):
        self.event.attendees.add(self.user)
        response = self.client.post(f'/events/{self.event.pk}/unregister/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.event.attendees.count(), 0)

    def test_search_event(self):
        response = self.client.get('/events/search/', {'q': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
