from django.contrib import admin

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


@admin.register(Post)
class PosttAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
