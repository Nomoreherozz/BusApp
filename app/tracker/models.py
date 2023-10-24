from django.db import models
import random

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
    plate = models.CharField(max_length=16)
    in_stop_id = models.PositiveIntegerField()
    velocity = models.FloatField()
    distance_from_src = models.FloatField()

    def get_velocity(self):
        self.velocity = round(random.uniform(0.0, 50.0), 2)
        return self.velocity
    
    def current_at(self):
        return self.in_stop_id
    
    def get_segment_length(self):
        stop = Station.objects.get(number=self.route, stop_id=str(self.current_at()))
        return stop.distance

    def get_drived_gap(self):
        self.distance_from_src += round(self.get_velocity()*5/18, 2)
        if self.distance_from_src > self.get_segment_length():
            self.distance_from_src -= self.get_segment_length()
            self.in_stop_id += 1
        return self.distance_from_src


    def get_distance(self):
        self.distance_from_src = self.get_drived_gap() 
        return round(self.distance_from_src, 2)
    
        
    def run(self):
        print("{:12} {:6} {:8}".format("m_from_src", "stop_id", "current_at"))
        for i in range(1000):
            print("{:10.2f} {:6} {:8}".format(self.get_distance(), self.in_stop_id, self.current_at()))
    
