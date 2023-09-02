from django.contrib import admin
from django.contrib.auth.models import User
from .models import Book, UserProfile, Discussion, Comment, ReadingGroup

# Register models for the admin interface
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(ReadingGroup)
