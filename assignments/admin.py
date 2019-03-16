from django.contrib import admin
from .models import AssignmentSubmissionForm, AssinmentType
# Register your models here.

class AssignmentsModelAdmin(admin.ModelAdmin):
    list_display = ["admission_number", "date", "full_name", "university"]
    list_display_links = ["date"]
    list_filter = ["date"]
    class Meta:
        model = AssignmentSubmissionForm
admin.site.register(AssignmentSubmissionForm, AssignmentsModelAdmin)

class AssignmentTypeModelAdmin(admin.ModelAdmin):
    list_display = ["type_of_assignment", "assignment_title","date", "unit_name", "unit_code"]
    list_display_links = ["assignment_title"]
    list_filter = ["date"]
    class Meta:
        model = AssinmentType
admin.site.register(AssinmentType, AssignmentTypeModelAdmin)