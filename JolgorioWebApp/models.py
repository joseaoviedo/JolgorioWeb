from django.db import models

class Actividad(models.Model):
    idactividad = models.AutoField(db_column='idActividad', primary_key=True)  # Field name made lowercase.
    tipo = models.IntegerField()
    titulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=300)
    enlace = models.CharField(max_length=50)
    descripcion_tmp = models.CharField(max_length=45)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Actividad'


class ActividadHasMaterial(models.Model):
    actividad_idactividad = models.OneToOneField(Actividad, models.DO_NOTHING, db_column='Actividad_idActividad', primary_key=True)  # Field name made lowercase.
    material_idmaterial = models.ForeignKey('Material', models.DO_NOTHING, db_column='Material_idMaterial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actividad_has_Material'
        unique_together = (('actividad_idactividad', 'material_idmaterial'),)


class Canton(models.Model):
    idcanton = models.AutoField(db_column='idCanton', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    idprovincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='idProvincia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Canton'


class Distrito(models.Model):
    iddistrito = models.AutoField(db_column='idDistrito', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    idcanton = models.ForeignKey(Canton, models.DO_NOTHING, db_column='idCanton')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Distrito'


class Logro(models.Model):
    idlogro = models.AutoField(db_column='idLogro', primary_key=True)  # Field name made lowercase.
    tipo = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Logro'


class Material(models.Model):
    idmaterial = models.AutoField(db_column='idMaterial', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Material'


class Pais(models.Model):
    idpais = models.AutoField(db_column='idPais', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Pais'


class Provincia(models.Model):
    idprovincia = models.AutoField(db_column='idProvincia', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    idpais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='idPais')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Provincia'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    iddistrito = models.ForeignKey(Distrito, models.DO_NOTHING, db_column='idDistrito')  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=100)
    fechanac = models.DateField(db_column='fechaNac')  # Field name made lowercase.
    numero = models.CharField(max_length=8)
    sexo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Usuario'


class UsuarioHasActividad(models.Model):
    usuario_idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='Usuario_idUsuario', primary_key=True)  # Field name made lowercase.
    actividad_idactividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='Actividad_idActividad')  # Field name made lowercase.
    fechacompletado = models.DateField(db_column='fechaCompletado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario_has_Actividad'
        unique_together = (('usuario_idusuario', 'actividad_idactividad'),)


class UsuarioHasLogro(models.Model):
    logro_idlogro = models.OneToOneField(Logro, models.DO_NOTHING, db_column='Logro_idLogro', primary_key=True)  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario_has_Logro'
        unique_together = (('logro_idlogro', 'usuario_idusuario'),)
