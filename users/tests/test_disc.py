from django.test import TestCase
from ..models import Forum

#Se consegue criar 1 discussão

class DiscussionTest(TestCase):
    def setUp(self):
        Forum.objects.filter().delete()
        Forum(title="forum1", body="Primeiro Forum").save()
        Forum(title="forum2", body="Segundo Forum").save()
        Forum(title="forum3", body="Terceiro Forum").save()

#se pega todos os foruns
    def test_get_all(self):
        forums = list(Forum.objects.values('title', 'body'))
        self.assertEqual(forums, [{'title': 'forum1', 'body': 'Primeiro Forum'}, {'title': 'forum2', 'body': 'Segundo Forum'}, {'title': 'forum3', 'body': 'Terceiro Forum'}])

#Ver se consegue achar o forum especifico
    def test_get_one(self):
        forum = list(Forum.objects.filter(title='forum1').values('title', 'body'))[0]
        self.assertEqual(forum, {'title': 'forum1', 'body': 'Primeiro Forum'})