from django.contrib import admin

from .models import Problem

# Register your models here.
class ProblemAdmin(admin.ModelAdmin):
    ...

admin.site.register(Problem, ProblemAdmin)