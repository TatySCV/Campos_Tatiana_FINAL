from django.db import models

class Institucion(models.Model):
    nombreInstitucion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreInstitucion

class Participantes(models.Model):

    ESTADOS_PARTICIPANTE = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombrePersona = models.CharField(max_length=80)
    telefono = models.IntegerField()
    fechaInscripcion = models.DateField() 
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    horaInscripcion = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS_PARTICIPANTE)
    observacion = models.CharField(max_length=255, blank=True)
    

class Autor(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    carrera = models.CharField(max_length=255)