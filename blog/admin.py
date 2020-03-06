from django.contrib import admin
from blog.models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'updatedatetime',)
    search_fields = ('title',)
    list_filter = ('owner',)

admin.site.register(Blog,BlogAdmin)