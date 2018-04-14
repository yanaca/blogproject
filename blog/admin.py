from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'modified_time', 'category', 'author']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
