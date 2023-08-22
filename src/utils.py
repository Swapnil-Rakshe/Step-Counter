import datetime


# Class Datapoint contains magnitude and corresponding time values 

class DataPoint:
    def __init__(self, mag, time):
        self.mag = mag  # Initialize the magnitude attribute
        self.time = time  # Initialize the time attribute
        
    def __str__(self):
         # Generate a string representation of the DataPoint
        ret = f"Acceleration magnitude is {self.mag} and time is {self.time}"
        return ret
    
    # Method to retrieve the time value of the DataPoint
    def getTime(self):
        return self.time 
    
     # Method to set the time value of the DataPoint
    def setTime(self, time):
        self.time = time  # Update the time attribute with the provided value
    
    # Method to retrieve the magnitude value of the DataPoint
    def getMagnitude(self):
        return self.mag # Return the magnitude attribute
    
    # Method to set the magnitude value of the DataPoint
    def setMagnitude(self, mag):
        self.mag = mag