from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src = "{}" width = "50" />'.format(object.photo.url))
    
    thumbnail.short_description = 'photo' # to change the name thumnail to photo 
    list_display = ('id','thumbnail','first_name','desigination','create_data') # ADD THE DESCRIPTION IN THE DATABASE
    list_display_links = ('id','first_name','desigination') # to make description clickable
    search_fields = ('first_name','last_name',)
    list_filter = ('desigination','last_name',)

admin.site.register(Team,TeamAdmin)