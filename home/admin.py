from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['Nombre_de_la_tarea', 'fecha_de_vencimiento', 'completado']


admin.site.register(Task, TaskAdmin)
