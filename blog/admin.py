from django.contrib import admin

from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "published_at"]
    list_select_related = ["post", "author"]
    autocomplete_fields = ["post", "author"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "published_at"]
    list_select_related = ["author"]
    autocomplete_fields = ["tags"]
    raw_id_fields = ["likes"]
    search_fields = ["title"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["title"]
