from tabnanny import verbose
from django.db import models
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Persona(models.Model):

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'Programador'),
        ('4', 'Desarrollador'),

    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    Habilidades = models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Personal de la empresa'
        ordering = ['last_name']

    def __str__(self):
        return self.last_name + ' ' + self.first_name 