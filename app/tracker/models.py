from django.db import models


class Station(models.Model):
    number = models.PositiveIntegerField()
    stop_id = models.CharField(max_length=16)
    name = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance = models.FloatField()

    def __str__(self):
        return str(self.number)


class Bus(models.Model):
    route = models.PositiveIntegerField()
    number_plate = models.CharField(max_length=16)
    latitude = models.FloatField()
    longitude = models.FloatField()
    velocity = models.FloatField()
    timestamp = models.CharField(max_length=16)


    def __str__(self):
        return str(self.route)
