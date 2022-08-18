from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester', email='tester@email.com', password='pass'
        )
        self.snack = Snack.objects.create(
            title='Kit Kat', description='Yum', purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'Kit Kat')

    def test_snack_content(self):
        self.assertEqual(f'{self.snack.title}', 'Kit Kat')
        self.assertEqual(f'{self.snack.purchaser}', 'tester')
        self.assertEqual(f'{self.snack.description}', 'Yum')

    def test_snack_list_view(self):
        response = self.client.get(reverse('list_snack'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kit Kat')
        self.assertTemplateUsed(response, 'snack-list.html')

    def test_snack_detail_view(self):
        response = self.client.get(reverse('detail_snack', args='1'))
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Purchaser: tester')
        self.assertTemplateUsed(response, 'snack-detail.html')

    def test_snack_create_view(self):
        response = self.client.post(
            reverse('create_snack'),
            {
                'title': 'Yum',
                'description': 'chocolate',
                'purchaser': self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse('detail_snack', args='2'))
        self.assertContains(response, 'Details about Yum')

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse('update_snack', args='1'),
            {'title': 'Updated title', 'description': 'new description', 'purchaser': self.user.id}
        )

        self.assertRedirects(response, reverse('detail_snack', args='1'))

    def test_snack_delete_view(self):
        response = self.client.get(reverse('delete_snacl', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_delete_view(self):
        response = self.client.get(reverse('delete_snack', args='1'))
        self.assertIsNot(response.status_code, 400)