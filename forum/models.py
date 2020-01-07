from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Rule(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True, null=True)
    sanction = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Thread(models.Model):
    class Meta:
        ordering = ['-created']

    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads', related_query_name='thread')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='threads',
                                 related_query_name='thread')
    rules = models.ManyToManyField(Rule, related_name='threads', related_query_name='thread', blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        ordering = ['-created']

    title = models.CharField(max_length=60)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    op = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', related_query_name='post')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts', related_query_name='post')
    tags = models.ManyToManyField(Tag, related_name='posts', related_query_name='post', blank=True)

    def __str__(self):
        return f'{self.pk} - {self.title}'


class Comment(models.Model):
    class Meta:
        ordering = ['-created']

    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')

    def __str__(self):
        return f'{self.pk}: ({self.post}) - {self.commenter.username}'
