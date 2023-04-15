from django.db import models


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    Prioridad = (('B', 'Baja'),
                 ('M', 'Media'),
                 ('A', 'Alta'))

    Nombre_de_la_tarea = models.CharField(max_length=200)
    fecha_de_vencimiento = models.DateTimeField(
        default=None, null=True, blank=True)
    completado = models.BooleanField(default=False)
    prioridad = models.CharField(max_length=1, choices=Prioridad, default='B')

    def __str__(self):
        return self.Nombre_de_la_tarea
