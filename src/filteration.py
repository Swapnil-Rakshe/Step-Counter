import pandas as pd
import numpy as np
import math
from datetime import datetime
from utils import DataPoint

class filteration:
    def __init__(self, ppData, filterLength = 13, filterSTD = 0.35):
        self.ppData = ppData
        self.filterLength = filterLength
        self.filterSTD = filterSTD
    
    def FilterStage(self):
        '''
        Second stage of step counting
        -----------------------------
            In order to reduce the noise level, algorithm implements a 
            finite impulse response (FIR) low-pass filter

        Parameters
        ----------
        ppData : list
            This ppData list is a output of preprocessing stage which contains DataPoints
        filterLength : int, optional
            The default is 13.
            length of window for a filter
        filterSTD : float, optional
            The default is 0.35.
            std dev for generating filter coefficients

        Returns
        -------
        smoothData : list
            smoothened data.

        '''

        midPoint = int(self.filterLength/2)
        filterVals = self.GenerateFilterCoef() # Generate filter coeff
        filterSum = sum(filterVals)
        inputQueue = self.ppData[:] #shallow copy
        smoothData = [] # output of filter stage
        active = True
        window = [] #list contains data point values

        while(active):
            window.append(inputQueue.pop(0))
            if(len(inputQueue) == 0):
                active = False
            
            if(len(window) == self.filterLength):
                temp = [v1*v2.getMagnitude() for v1,v2 in zip(filterVals, window)]
                acc_new_mag = sum(temp)/filterSum
                dp = DataPoint(acc_new_mag, window[midPoint].getTime())
                smoothData.append(dp)
                window.pop(0)
        #print('filter stage:', smoothData)      
        return smoothData

    def GenerateFilterCoef(self):
    
        '''
        Generate the filter coefficients based on the filter length and std dev

        Parameters
        ----------
        filterLength : int, optional
        length of filter. The default is 13.
        filterSTD : float, optional
        std dev. The default is 0.35.

        Returns
        -------
        FIR_Vals : list
        filter coefficients.

        '''
    
        FIR_Vals = [math.pow(math.e, -0.5*math.pow((i - (self.filterLength - 1)/2) / 
                 (self.filterSTD * (self.filterLength - 1)/2), 2)) for i in range(self.filterLength)]
    
        return FIR_Vals