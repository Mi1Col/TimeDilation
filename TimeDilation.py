import math

class TimeDilation:
    G = 6.67430e-11
    c = 3e8
    def __init__(self, time, distance, mass) -> None:
        self.time = time
        self.distance = distance
        self.mass = mass

    def criticalDistance(self):
        criticalDistance = (2 * self.G * self.mass) / (self.c**2)
        return criticalDistance
    
    def dilationFactor(self):
        if self.distance <= self.criticalDistance():
            return ValueError
        else:
            return math.sqrt(1 - (2 * self.G * self.mass) / (self.c ** 2 * self.distance))
    
    def relativeTime(self):
        dilationFactor = self.dilationFactor()
        if dilationFactor == ValueError:
            return "ERROR: Critical distance has been reached."
        relativeTime = self.time * self.dilationFactor()
        return relativeTime


