from django.db import models


# Create your models here.
class reservaciones(models.Model):
    id_cliente = models.IntegerField()
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    num_personas = models.IntegerField()

    def __str__(self):
        return f"reservacion - {self.fecha_reserva} a las {self.hora_reserva}"