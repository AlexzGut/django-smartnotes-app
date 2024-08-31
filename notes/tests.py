from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.http import urlencode
from .models import Notes

class NotesIndexViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')

    def test_no_notes(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('notes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Start adding notes')
        self.assertQuerySetEqual(response.context['notes'], [])

    def test_notes(self):
        # create a Notes object
        note = Notes(title='Test note', text='This is a test note')
        # creates a relation between the user and the note previoulsy created.
        # self.user have one note
        note.user = self.user
        # save the Notes object to the test database
        note.save()
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('notes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['notes'], [note])

class NotesDetailViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')

    def test_note_does_not_exist(self):
        # notes/<int:pk> receives a primary key as a url parameter
        pk = 1
        response = self.client.get(reverse('notes:detail', args=(pk,)))
        self.assertEqual(response.status_code, 404)
    
    def test_note_exists(self):
        note = Notes(title='Test note', text='This is a test note')
        note.user = self.user
        note.save()
        response = self.client.get(reverse('notes:detail', args=(note.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, note.title)

class NotesCreateViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')

    # test the -GET request-
    def test_create_note_with_user_loggedin_get(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('notes:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/form.html')

    def test_create_note_with_user_not_loggedin_get(self):
        response = self.client.get(reverse('notes:create'))
        # HTTP status code 302 indicates a 'temporary redirect'. When the user has not logged in
        # the user will be redirected to the login page
        self.assertEqual(response.status_code, 302)
        # generates the url for login a user
        login_url = reverse('login')
        # generates the url to create a new note
        next_url = reverse('notes:create')
        # encodes the `next` query parameter to be appended to the login url
        # this is the url Django uses to redirect the user for login and then to create a new note
        redirect_url = f'{login_url}?{urlencode({'next': next_url})}'
        self.assertRedirects(response, redirect_url)

    # test the form submission -POST request-
    def test_create_note_with_user_loggedin_post(self):
        self.client.login(username='testuser', password='secret')
        note_data = {"title": "Test note", "text": "This is a test note"}
        response = self.client.post(reverse('notes:create'), note_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Notes.objects.filter(title='Test note').exists())
