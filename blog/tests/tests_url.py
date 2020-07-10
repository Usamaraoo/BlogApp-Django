from django.test import TestCase
from django.utils import timezone
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import *
from blog.models import About, BlogPost

# class TestUrl(SimpleTestCase):
#     def test_list_url_resolved(self):
#         url = reverse('list')
#         print(resolve(url))
#         self.assertEqual(resolve(url).func, blog_list_view)
#
#     def test_detail_url_resolved(self):
#         url = reverse('detail')
#         print(resolve(url))
#         self.assertEqual(resolve(url).func, blog_create_view)


class AnimalTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(title="lion", content="roar", slug="pop", publish_date=timezone.now())
