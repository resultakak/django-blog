from django.contrib import admin
from blog.models import Category, Post

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'created_at', 'update_at'
    )


admin.site.register(Post, PostAdmin)
