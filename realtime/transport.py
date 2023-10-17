import random
import json
import time


data = open("data/39.json", encoding="utf-8")
buses = json.load(data)

class Bus():
    """The Bus class contains many functions and attributes such as speed, location.

    Returns:
        object: Bus object.
    """

    def __init__(self, number, bus_id=None, in_segment_id=1, velocity=0.0, distance_from_src=0.0, **kwargs) -> None:
        if not isinstance(number, int) or not number >= 0:
            print("[!] Please enter a positive integer for the bus's number.")
        else:
            self.number = str(number)


        # if not isinstance(bus_id, str) or not number >= 0:
        #     print("[!] Please enter the bus's id (ex: '51F-00818, 62B-12345').")
        # else:
        #     self.bus_id = bus_id


        if not isinstance(in_segment_id, int) or not in_segment_id >= 0:
            print("[!] Please enter a positive integer for the stop's id.")
        else:
            self.in_segment_id = in_segment_id

        if not isinstance(velocity, float) or not velocity >= 0.0:
            print("[!] Please enter a positive float for the velocity.")
        else:
            self.velocity = velocity


        if not isinstance(distance_from_src, float):
            print("[!] Please enter a positive float for the distance from start_stop in (m).")
        elif distance_from_src >= 0.0:
            for bus in buses:
                if bus["stop_id"] == in_segment_id:
                    if distance_from_src > bus["distance(m)"]:
                        print("[!] The distance to the next stop is over the length.")
                    else:
                        self.distance_from_src = distance_from_src


        # if "reach_at_time" == None:
        #     # print("[!] Please enter the check-in time of the next stop.")
        #     pass
        # else:
        #     # self.reach_at_time = kwargs["reach_at_time"]
        #     pass


    def get_velocity(self):
        self.velocity = round(random.uniform(0.0, 50.0), 2)
        return self.velocity
    

    def get_segment_length(self):
        for bus in buses:
            if bus["stop_id"] == self.current_at():
                return bus["distance(m)"]


    def current_at(self):
        return self.in_segment_id
    
    
    def get_drived_gap(self):
        
        self.distance_from_src += round(self.get_velocity()*5/18, 2)
        if self.distance_from_src > self.get_segment_length():
            self.distance_from_src -= self.get_segment_length()
            self.in_segment_id += 1
        return self.distance_from_src


    def get_distance(self):
        self.distance_from_src = self.get_drived_gap()
    
        return round(self.distance_from_src, 2)
    
        
    def run(self):
        print("{:12} {:6} {:8}".format("m_from_src", "stop_id", "current_at"))
        for i in range(1000):
            print("{:10.2f} {:6} {:8}".format(self.get_distance(), self.in_segment_id, self.current_at()))


a = Bus(number=39)
a.run()