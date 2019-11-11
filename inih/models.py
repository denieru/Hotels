from django.db import models

# Create your models here.
from django.utils import timezone


class inih(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descr1 = models.TextField()
    descr2 = models.TextField()
    fecha_c = models.DateTimeField(
            default=timezone.now)
    fecha_p = models.DateTimeField(
            blank=True, null=True)

    def inicioh(self):
        self.fecha_p = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    