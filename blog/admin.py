from django.contrib import admin
from .models import Post, Image

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class ImageInline(admin.TabularInline):
    model = Image

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Post, PostAdmin)
