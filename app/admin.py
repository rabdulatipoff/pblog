from django.contrib import admin
from .models import Post

def publish_posts(modeladmin, request, queryset):
    for post in queryset:
        post.publish()
publish_posts.short_description = "Publish the selected posts"

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']
    ordering = ['published_date']
    actions = [publish_posts]

admin.site.register(Post, PostAdmin)
