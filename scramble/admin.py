from django.contrib import admin
from scramble.models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display =  ['name','par','location']

admin.site.register(Course, CourseAdmin)