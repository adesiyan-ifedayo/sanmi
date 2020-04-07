from django.contrib import admin
from .models import Post, Contact, Aboutme, Comment

# Register your models here.


app_name = 'core'

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Aboutme)
admin.site.register(Comment)

admin.site.site_header = 'SanmiArt Administration'