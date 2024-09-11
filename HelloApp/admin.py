from django.contrib import admin
from HelloApp.models import *

admin.site.register(BlogData)
admin.site.register(Person)

# Register your models here.

class BioDataAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'gender']
    list_editable = ['gender']
    search_fields = ['lname']

admin.site.register(BioData, BioDataAdmin)