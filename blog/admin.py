from django.contrib import admin
from blog.models import Category, Post, Comment, Contact

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = (
        'title', 'created_at', 'updated_At'
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'updated_At')
    search_fields = ('author__username',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'created_at')
    search_fields = ('email',)
