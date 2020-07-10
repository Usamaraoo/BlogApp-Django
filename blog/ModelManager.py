from django.utils import timezone
from django.db import models


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)


# using Manager for filtering queryset
class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self.db)

    # by using published we can use just BlogPost.objects.all().published()
    # or BlogPost.objects.published()
    def published(self):
        return self.get_queryset().published()
