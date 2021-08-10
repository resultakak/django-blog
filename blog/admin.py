from django.contrib import admin
from blog.models import Category, Post, Comment

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = (
        'title', 'created_at', 'update_at'
    )


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'updated_At')
    search_fields = ('author__username',)


admin.site.register(Comment, CommentAdmin)
