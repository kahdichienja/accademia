from django.contrib import admin
from . models import University, NotesUpload
# Register your models here.

class NotesModelAdmin(admin.ModelAdmin):
    list_display = ["unit_name","timestamp","unit_code"]
    list_display_links = ["unit_code"]
    list_filter = ["unit_code"]
    search_fields = ["unit_code","unit_name"]
    class Meta:
        model = NotesUpload

admin.site.register(NotesUpload, NotesModelAdmin)

class UniversityModelAdmin(admin.ModelAdmin):
    list_display = ["name","timestamp"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["unit_code","name"]
    class Meta:
        model = University

admin.site.register(University, UniversityModelAdmin)