from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'watched', 'is_published', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'author', 'created_at', 'updated_at')
    list_editable = ('is_published',)
    readonly_fields = ('watched',)

admin.site.register(Category)
admin.site.register(Post , PostAdmin)
