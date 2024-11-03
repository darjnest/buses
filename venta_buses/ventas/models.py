from django.db import models


class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    duracion_estimada = models.DurationField()

    def __str__(self):
        return f"{self.origen} - {self.destino}"


class Horario(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()

    def __str__(self):
        return f"{self.ruta} | {self.hora_salida} - {self.hora_llegada}"


class Bus(models.Model):
    numero_bus = models.CharField(max_length=10)
    capacidad = models.IntegerField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bus {self.numero_bus} | {self.horario}"


class Boleto(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now_add=True)
    nombre_pasajero = models.CharField(max_length=100)
    documento_identidad = models.CharField(max_length=20)

    def __str__(self):
        return f"Boleto para {self.nombre_pasajero} en {self.bus}"
