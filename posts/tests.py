from django.test import TestCase

# Create your tests here.
from .models import Post

class PostModelTest(TestCase):
    def setUp(Test):
        Post.objects.create(text = 'some text')
        
    def testSetContent(self):
        post = Post.objects.get(id=1)
        name = f'{post.text}'
        self.assertEqual(name, 'sometext')
