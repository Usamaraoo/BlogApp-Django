from django.db import models
from django.conf import settings
from .ModelManager import BlogPostManager

# Create your models here.
User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    # id = models.IntegerField() # pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('About', on_delete=models.CASCADE)
    objects = BlogPostManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date', '-updated', 'timestamp']

    # these methods for maping urls in templates
    def get_absolute_url(self):
        return f"/{self.slug}"

    def get_edit_url(self):
        return f'/{self.slug}/edit'

    def get_delete_url(self):
        return f"/{self.slug}/delete"


class About(models.Model):
    topics = models.CharField(max_length=30)
    blogs = models.ManyToManyField(BlogPost)

    def __str__(self):
        return self.topics

    class Meta:
        verbose_name_plural = 'related'
