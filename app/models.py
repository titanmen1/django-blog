from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='category',
        blank=True, null=True
    )
    tags = models.ManyToManyField('Tag', related_name='tags', blank=True)
    status = models.CharField(max_length=64, choices=[('p', 'published'), ('d', 'draft')])

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'# {self.id} - {self.author}'


class Tag(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'
