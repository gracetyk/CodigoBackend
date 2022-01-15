from django.db import models

# Create your models here.

class PersonaModel(models.Model):
    opcionesEstadoCivil=[
        ('SOLTERO','SOLTERO')
        ('CASADO','CASADO')
        ('VIUDO','VIUDO')
        ('DIVORCIADO','DIVORCIADO')
        ('COMPLICADO','COMPLICADO')
        ('NO _ESPECIFICA','NO _ESPECIFICA')]

    personaId=models.AutoField(
        primary_key=True, 
        unique=True,
        null=False,
        db_column='id')

    personaNombre=models.CharField(
        max_legth=50,
        unique=False,
        null=False,
        db_column='nombre')
    
    personaApellido = models.CharField(
        max_length=50,  
        unique=False,
        null=False,
        db_column='apellido'
    )

    personaEmail=models.EmailField(
        max_length=50,  
        unique=True,
        null=False, 
        db_column='email'
    )

    personaFechaNacimiento=models.DateField(
        db_column='fec_nac' ,
    )

    personaEstadoCivil=models.CharField(
        choices=opcionesEstadoCivil,
        db_column='estado_civil',
        default='SOLTERO'
    )

    personaFoto=models.ImageField(
        db_column='foto',
        upload_to='personas/'#carpeta donde se almacenaràn los archivos
    )