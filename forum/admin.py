from django.contrib import admin

from .models import Category, Thread, Post, Comment, Rule, Tag

admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Rule)
admin.site.register(Tag)
