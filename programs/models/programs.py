
# Django
from django.db import models

# Models
from django.contrib.auth.models import User
from programs.models import ProgrammingLanguage
from projects.models import Module

# Utils
from projects.validators import validate_min_length_description


class Program(models.Model):
    name = models.CharField(max_length=100, help_text='Program name')
    description = models.CharField(max_length=200, validators=[validate_min_length_description])
    programmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='program_user')
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, related_name='program_language')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='program_module')

    total_lines = models.IntegerField(default=0)
    
    planning_date = models.DateField()
    start_date = models.DateField()
    finish_date = models.DateField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Pip(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='list_pip_program')
    name = models.CharField(max_length=100, help_text='Pip name')
    date = models.DateTimeField()
    
    problems = models.TextField(max_length=350)
    proposal = models.TextField(max_length=350)
    comment = models.TextField(max_length=350)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='reports_view')
    name = models.CharField(max_length=100, help_text='Report name')
    date = models.DateTimeField()

    objetive = models.TextField(max_length=350)
    description = models.TextField(max_length=350)
    conditions = models.TextField(max_length=350)
    expect_results = models.TextField(max_length=350)
    current_results = models.TextField(max_length=350, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    



    