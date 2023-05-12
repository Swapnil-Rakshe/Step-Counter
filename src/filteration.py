
import math
from utils import DataPoint

class filteration:
    def __init__(self):
        pass
    
    def FilterStage(self, ppData, filterLength = 13):

        midPoint = int(filterLength/2)
        filterVals = self.GenerateFilterCoef() # Generate filter coeff
        filterSum = sum(filterVals)
        inputQueue = ppData[:] #shallow copy
        smoothData = [] # output of filter stage
        active = True
        window = [] #list contains data point values

        while(active):
            window.append(inputQueue.pop(0))
            if(len(inputQueue) == 0):
                active = False
            
            if(len(window) == filterLength):
                temp = [v1*v2.getMagnitude() for v1,v2 in zip(filterVals, window)]
                acc_new_mag = sum(temp)/filterSum
                dp = DataPoint(acc_new_mag, window[midPoint].getTime())
                smoothData.append(dp)
                window.pop(0)
        #print('filter stage:', smoothData)      
        return smoothData

    def GenerateFilterCoef(self,filterLength = 13, filterSTD = 0.35):
    
        FIR_Vals = [math.pow(math.e, -0.5*math.pow((i - (filterLength - 1)/2) / 
                 (filterSTD * (filterLength - 1)/2), 2)) for i in range(filterLength)]
    
        return FIR_Vals