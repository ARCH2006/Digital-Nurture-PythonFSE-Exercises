from django.contrib import admin
from .models import Course,Department,Student,Enrollment

admin.site.register(Department)

admin.site.register(Student)

admin.site.register(Enrollment)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name",'code','credits','department']
    search_fields = ['name','department']
    list_filter = ['department']


# Register your models here.
