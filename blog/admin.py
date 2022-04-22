from django.contrib import admin
from blog.models import Tag, Post,Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

# Register your models here.

admin.site.register(Tag)1
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

