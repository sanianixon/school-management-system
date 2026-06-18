from django.contrib import admin
from .models import School, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'enrollment', 'school', 'created_at')
    search_fields = ('name', 'enrollment')
    list_filter = ('school',)
    ordering = ('id',)