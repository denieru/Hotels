from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class config(models.Model):
    Usuario= models.ForeignKey('UserProfile', null=True,blank=True, related_name='config', on_delete=models.PROTECT)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True,on_delete=models.PROTECT)
    karma = models.IntegerField(default=0, blank=True)
    def __str__(self):
        return self.user.username


class inih(models.Model):
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
    
class menu(models.Model):
    nombrem = models.CharField(max_length = 50)
    subm = models.ForeignKey('self', null=True,blank=True, related_name='menu', on_delete=models.PROTECT)
    fecha_cm = models.DateTimeField(
            default=timezone.now)
    fecha_pm = models.DateTimeField(
            blank=True, null=True)
    def menuh(self):
        self.fecha_pm = timezone.now()
        self.save()
    def __str__(self):
        return self.nombrem

class servh(models.Model):
   
    titulo = models.CharField(max_length=200)
    descr = models.TextField()
    INACTIVO = 0
    ACTIVO = 1
    STATUS = (
        (INACTIVO,('Inactive')),
        (ACTIVO,('Active')),
    )

    status  = models.BooleanField(default=0, choices=STATUS)
    fecha_c = models.DateTimeField(
            default=timezone.now)
    fecha_p = models.DateTimeField(
            blank=True, null=True)

    def servih(self):
        self.fecha_p = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class archivo(models.Model):
    file = models.FileField(blank=False, null=False)
    fecha_c = models.DateTimeField(
            default=timezone.now)
    fecha_p = models.DateTimeField(
            blank=True, null=True)

    def arch(self):
        self.fecha_p = timezone.now()
        self.save()

    def __str__(self):
        return self.file.name

class habh(models.Model):
   
    titulo = models.CharField(max_length=200)
    descr = models.TextField()
    F_servicio = '0'
    Desocupada = '1'
    Ocupada = '2'
    Reservada = '3' 
    STATUS = (
        (F_servicio,('Inactive')),
        (Desocupada,('Desocupada')),
        (Ocupada,('Ocupada')),
        (Reservada,('Reservada')),
    )

    status  = models.CharField(max_length=2,default=0, choices=STATUS)
    fecha_c = models.DateTimeField(
            default=timezone.now)
    fecha_p = models.DateTimeField(
            blank=True, null=True)

    def servih(self):
        self.fecha_p = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
