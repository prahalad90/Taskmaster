from django.contrib import admin
from .models import taskmaster, terms

# Register your models here.
@admin.register(taskmaster)
class TaskMasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'date','task', 'enquiryNo','timetaken', 'comments','userid']

@admin.register(terms)
class TermAdmin(admin.ModelAdmin):
    list_display = ['id', 'taskName',]