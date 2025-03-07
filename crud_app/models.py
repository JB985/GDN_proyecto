from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    cod = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    TIPO_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('OT', 'Otro')
    ]
    tip_documento = models.CharField(max_length=100, null=False, choices=TIPO_DOCUMENTO, default='CC')
    num_documento = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=10, null=False)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, default='APRENDIZ')

    def __str__(self):
        return self.username

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)#+
    cod_sub = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)

class Category(models.Model):
    id = models.AutoField(primary_key=True)#+
    cod_cat = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False)

class Moviliario(models.Model):
    name = models.CharField(max_length=100, null=False, default='nombre')
    desc = models.TextField(blank=True, null=True)
    ad_date = models.DateField(null=False)
    num_placa_almacen = models.CharField(max_length=45, null=False, unique=True, default='placa')
    price = models.DecimalField(max_length=20, decimal_places=2, max_digits=20, null=False, default='00000')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

class Regional(models.Model):
    cod_reg =  models.CharField(max_length=255, unique=True, null=False)
    name = models.CharField(max_length=255, unique=True, null=False)

class CentroFormacion(models.Model):
    nit = models.CharField(max_length=20, null=False, unique=True)
    name = models.CharField(max_length=200, null=False)
    reg = models.ForeignKey(Regional, on_delete=models.CASCADE, null=False)

class Sede(models.Model):
    cod_sede = models.CharField(max_length=255, unique=True, null=False)
    name = models.CharField(max_length=255, unique=True, null=False)
    city = models.CharField(max_length=255, null=False)
    direct = models.CharField(max_length=255, null=False)
    reg = models.ForeignKey(Regional, on_delete=models.CASCADE, null=False)

class Programa_Formacion(models.Model):
    cod_prog = models.CharField(max_length=255, unique=True, null=False)
    name = models.CharField(max_length=255, unique=True, null=False)
    hours = models.IntegerField(null=False)
    version = models.CharField(max_length=255, null=False)

class Ficha(models.Model):
    num_ficha = models.CharField(max_length=255, unique=True, null=False)
    name = models.CharField(max_length=255, null=False)
    etapa = models.CharField(max_length=255, null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=False)
    prog = models.ForeignKey(Programa_Formacion, on_delete=models.CASCADE, null=False)