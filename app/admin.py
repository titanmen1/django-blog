from django.contrib import admin

# Register your models here.
from app.models import Post, Tag, Category

admin.site.register([Post, Tag, Category])
