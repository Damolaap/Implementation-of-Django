from django.contrib import admin
from BlogApp.models import *

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Comments)
admin.site.register(Category)