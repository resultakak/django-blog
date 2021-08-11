from django.db import models
from blog.models import Post
from blog.abstract_models import DateAbstractModel

class Comment(DateAbstractModel):
    author = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.comment
