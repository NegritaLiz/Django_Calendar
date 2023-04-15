from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Task
from django.db import models
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Nombre_de_la_tarea', 'fecha_de_vencimiento']
        
    def clean(self):
        cleaned_data = super().clean()
        nombre_tarea = cleaned_data.get('Nombre_de_la_tarea')
        if not nombre_tarea:
            self.add_error('Nombre_de_la_tarea', _(
                'El nombre de la tarea es un campo requerido.'))


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Nombre_de_la_tarea',
                  'fecha_de_vencimiento', 'prioridad', 'completado']
