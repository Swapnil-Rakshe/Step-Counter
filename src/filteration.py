
import math
# Import the DataPoint class from the 'utils' module
from utils import DataPoint

# Define a class named 'filteration'
class filteration:
    def __init__(self):
        pass
    
    def FilterStage(self, ppData, filterLength = 13):
        # Method for filtering the input data
        midPoint = int(filterLength/2)
        filterVals = self.GenerateFilterCoef() # Generate filter coeff
        filterSum = sum(filterVals) # Generate filter coefficients using the method
        inputQueue = ppData[:] #shallow copy
        smoothData = [] # output of filter stage
        active = True
        window = [] #list contains data point values

        # Iterate while active flag is True
        while(active):
            window.append(inputQueue.pop(0))  # Add a data point to the window
            if(len(inputQueue) == 0): # Check if the input queue is empty
                active = False  # Set active flag to False to exit the loop
            
            if(len(window) == filterLength):
                temp = [v1*v2.getMagnitude() for v1,v2 in zip(filterVals, window)]
                acc_new_mag = sum(temp)/filterSum
                dp = DataPoint(acc_new_mag, window[midPoint].getTime())
                smoothData.append(dp) # Add the new DataPoint to the smoothed data
                window.pop(0) # Remove the oldest data point from the window
        #print('filter stage:', smoothData)      
        return smoothData

    # Method to generate filter coefficients using the Gaussian distribution
    def GenerateFilterCoef(self,filterLength = 13, filterSTD = 0.35):
    
        FIR_Vals = [math.pow(math.e, -0.5*math.pow((i - (filterLength - 1)/2) / 
                 (filterSTD * (filterLength - 1)/2), 2)) for i in range(filterLength)]
    
        return FIR_Vals # Return the generated filter coefficients