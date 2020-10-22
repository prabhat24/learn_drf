from django.contrib import admin
from .models import Post
# Register your models here.


from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
