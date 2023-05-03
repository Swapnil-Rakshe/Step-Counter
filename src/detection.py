import pandas as pd
import numpy as np
import math
from datetime import datetime

class detection:
    def __init__(self, peakScoreData, threshold = 1.2):
        self.peakScoreData = peakScoreData
        self.threshold = threshold
    
    def DetectionStage(self):
    
        '''
    Fourth stage of step counting
    -----------------------------
        This stage identifies potential candidate peaks to be associated with a 
        step by statistically detecting outliers. 
        As the algorithm processes the signal, it keeps track of a running mean 
        and standard deviation. These two quantities are used to determine 
        whether any given sample is an outlier.

    Parameters
    ----------
    peakScoreData : list
        list containing peakiness values.
    threshold : float, optional
        detection threshold. The default is 1.2 assuming the sampling frequency is 100Hz.

    Returns
    -------
    outputQueue : list
        output list containing DataPoints.

        '''
    
        inputQueue = self.peakScoreData[:] # Shallow copy
        outputQueue = []
        # initial parameters
        active = True
        count = 0
        acc_mean = 0
        acc_std = 0

        while(active):
            dp = inputQueue.pop(0)
            if(len(inputQueue) == 0):
                active = False
                # dp = DataPoint(0, 0)
                # outputQueue.append(dp)
                # continue
            count +=1
            o_mean = acc_mean
        
            # Update calculations of mean and std deviation
            if(count == 1):
                acc_mean = dp.getMagnitude()
                acc_std = 0
            elif(count == 2):
                acc_mean = (acc_mean + dp.getMagnitude())/2
                acc_std = (((dp.getMagnitude() - acc_mean)**2 + (o_mean - acc_mean)**2 ) ** 0.5)/2            
            else:
                acc_mean = (dp.getMagnitude() + (count - 1)*acc_mean)/count
                acc_std = (((count - 2) * (acc_std**2)/(count-1)) + (o_mean - acc_mean)**2 + ((dp.getMagnitude() - acc_mean) ** 2)/count)**0.5
        
            # Once we have enough data points to have a reasonable mean/standard deviation, start detecting
            if(count >= 1): #Min data points to be counted is 1 data point
                if ((dp.getMagnitude() - acc_mean) > acc_std * self.threshold):
                    # This is peak
                    outputQueue.append(dp)
    
        #print('detection stage:', outputQueue)
        return outputQueue