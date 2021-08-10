from django.db import models
from autoslug import AutoSlugField
from blog.models import Category
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=70)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    cover = models.ImageField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title
