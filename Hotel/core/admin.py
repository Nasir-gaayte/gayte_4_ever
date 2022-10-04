from atexit import register
from django.contrib import admin
from .models import PostModel, Category, CommentModel

# Register your models here.


admin.site.register(PostModel)
admin.site.register(Category)
admin.site.register(CommentModel)

## what