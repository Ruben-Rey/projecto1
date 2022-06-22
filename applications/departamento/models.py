from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, editable=False)
    shor_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return self.shor_name