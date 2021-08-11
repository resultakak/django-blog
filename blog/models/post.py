from django.db import models
from autoslug import AutoSlugField
from blog.models import Category
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel

class Post(DateAbstractModel):
    title = models.CharField(max_length=70)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = RichTextField()
    categories = models.ManyToManyField(Category)
    cover = models.ImageField(upload_to='post')
    author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title
