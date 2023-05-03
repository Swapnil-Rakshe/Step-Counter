import datetime


# Class Datapoint contains magnitude and corresponding time values 

class DataPoint:
    def __init__(self, mag, time):
        self.mag = mag
        self.time = time
        
    def __str__(self):
        ret = f"Acceleration magnitude is {self.mag} and time is {self.time}"
        return ret
    
    def getTime(self):
        return self.time 
        
    def setTime(self, time):
        self.time = time
        
    def getMagnitude(self):
        return self.mag
    
    def setMagnitude(self, mag):
        self.mag = mag