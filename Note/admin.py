from django.contrib import admin
from Note.models import MyNote

class adminNote(admin.ModelAdmin):
    list_display = ('title','content')

admin.site.register(MyNote,adminNote)

# Register your models here.
