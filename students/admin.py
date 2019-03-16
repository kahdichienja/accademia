from django.contrib import admin
from .models import StudentRegisterForm
# Register your models here.
class StudentsModelAdmin(admin.ModelAdmin):
    list_display = ["first_name","surname","admission_number","last_name","university","timestamp"]
    list_display_links = ["university"]
    list_filter = ["admission_number", "university"]
    search_fields = ["university","university"]
    class Meta:
        model = StudentRegisterForm

admin.site.register(StudentRegisterForm, StudentsModelAdmin)