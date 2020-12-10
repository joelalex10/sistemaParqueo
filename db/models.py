# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alquiler(models.Model):
    id_alquiler = models.AutoField(primary_key=True)
    inicio = models.DateField()
    fin = models.DateField()
    cliente_id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_id_cliente')
    id_tarifa_alquiler = models.ForeignKey('TarifaAlquiler', models.DO_NOTHING, db_column='id_tarifa_alquiler')

    class Meta:
        managed = False
        db_table = 'alquiler'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=30)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cliente'


class ControlHorario(models.Model):
    id_control_horario = models.AutoField(primary_key=True)
    fecha = models.DateField()
    ingreso = models.TimeField()
    salida = models.TimeField()
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'control_horario'


class Descuento(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    monto = models.FloatField()

    class Meta:
        managed = False
        db_table = 'descuento'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=45)
    nombre = models.CharField(max_length=30)
    razon_social = models.CharField(max_length=40)
    direccion = models.TextField()
    contacto = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'empresa'


class Espacio(models.Model):
    id_espacio = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=30)
    id_tipo_espacio = models.ForeignKey('TipoEspacio', models.DO_NOTHING, db_column='id_tipo_espacio')

    class Meta:
        managed = False
        db_table = 'espacio'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    codigo_control = models.CharField(max_length=30)
    autorizacion = models.IntegerField()
    empresa_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_id_empresa')
    alquiler_id_alquiler = models.ForeignKey(Alquiler, models.DO_NOTHING, db_column='alquiler_id_alquiler')
    registro_parqueo_id_parqueo = models.ForeignKey('RegistroParqueo', models.DO_NOTHING, db_column='registro_parqueo_id_parqueo')

    class Meta:
        managed = False
        db_table = 'factura'


class Incidentes(models.Model):
    id_incidentes = models.AutoField(primary_key=True)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'incidentes'


class PlanPagos(models.Model):
    id_plan_de_pagos = models.AutoField(primary_key=True)
    monto_cuota = models.FloatField()
    num_cuotas = models.IntegerField()
    cuotas_pagadas = models.IntegerField()
    alquiler_id_alquiler = models.ForeignKey(Alquiler, models.DO_NOTHING, db_column='alquiler_id_alquiler')

    class Meta:
        managed = False
        db_table = 'plan_pagos'


class RegistroCaja(models.Model):
    id_registro_caja = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    monto = models.FloatField()
    tipo = models.CharField(max_length=40)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'registro_caja'


class RegistroParqueo(models.Model):
    id_parqueo = models.AutoField(primary_key=True)
    entrada = models.DateTimeField()
    salida = models.DateTimeField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING)
    id_espacio = models.ForeignKey(Espacio, models.DO_NOTHING, db_column='id_espacio')
    id_tarifas = models.ForeignKey('Tarifa', models.DO_NOTHING, db_column='id_tarifas')
    id_descuento = models.ForeignKey(Descuento, models.DO_NOTHING, db_column='id_descuento')
    incidentes_id_incidentes = models.ForeignKey(Incidentes, models.DO_NOTHING, db_column='incidentes_id_incidentes')

    class Meta:
        managed = False
        db_table = 'registro_parqueo'


class Tarifa(models.Model):
    id_tarifas = models.AutoField(primary_key=True)
    horas = models.IntegerField()
    dias = models.IntegerField()
    precio = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tarifa'


class TarifaAlquiler(models.Model):
    id_tarifa_alquiler = models.AutoField(primary_key=True)
    meses = models.IntegerField()
    precio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tarifa_alquiler'


class TipoEspacio(models.Model):
    id_tipo_espacio = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_espacio'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class TipoVehiculo(models.Model):
    id_tipo_vehiculo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_vehiculo'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=30)
    nombre = models.CharField(max_length=45)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    hora_ingreso = models.TimeField(blank=True, null=True)
    hora_salida = models.TimeField(blank=True, null=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehiculo'
