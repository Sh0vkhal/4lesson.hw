from django.contrib import admin

# Register your models here.

from .models import Category, Moview,Comment

admin.site.register(Category)
admin.site.register(Moview)
admin.site.register(Comment)