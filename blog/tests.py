from django.test import TestCase
from .models import Post
# Create your tests here.

class PostTest(TestCase):
    def test_post_creation(self):
        art = Post(title = 'Arbol', text = 'Hola, buen dia', post = 1)
        art.save()

        self.assertEqual(art.title, 'Arbol')
        self.assertEqual(art.text, 'Hola, buen dia')