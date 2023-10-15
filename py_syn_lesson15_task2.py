class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"
    
class Autobus(Transport):
    capacity = 50
    
    def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name} {self.capacity} пассажиров"


A1 = Autobus("Renault Logan", 90, 10293)
print(A1.seating_capacity())