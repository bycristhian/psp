
# Django
from django.db import models

# Models
from projects.models import Project
from django.utils.datetime_safe import new_datetime

# Validators
from projects.validators import validate_min_length_description


class Module(models.Model):
    name = models.CharField(max_length=100, help_text='Module name')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='modules')
    description = models.CharField(max_length=200, help_text='Module description', validators=[validate_min_length_description])

    planning_date = models.DateField()
    start_date = models.DateField()
    finish_date = models.DateField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
