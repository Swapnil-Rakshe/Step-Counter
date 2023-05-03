import pandas as pd
import numpy as np
import math
from datetime import datetime
from utils import DataPoint

class scoring:
    def __init__(self, smoothData, windowSize = 35):
        self.smoothData = smoothData
        self.windowSize = windowSize
    
    def ScoringStage(self):
    
        '''
    Third stage of step counting
    ----------------------------
        The function of the scoring stage is to evaluate the peakiness of a given 
        sample. The result of this stage should increase the magnitude of any 
        peaks, making them more evident for the subsequent peak detection.

    Parameters
    ----------
    smoothData : list
        list containing smoothened datapoint values
    windowSize : int, optional
        window size for score peak calculation. The default is 35.

    Returns
    -------
    peakScoreData : list
        output of scoring stage.

        '''
    
        midPoint = int(self.windowSize/2) #Mid point of window
        inputQueue = self.smoothData[:] # shallow copy
        peakScoreData = [] 
        window = [] #list containing magnitude values
        active = True

        while(active):
            window.append(inputQueue.pop(0))
            if(len(inputQueue) == 0):
                active = False
            
            if(len(window) == self.windowSize):
                diffLeft = 0
                diffRight = 0
                # calculate diffleft and diffright based on the algorithm
                for i in range(midPoint):
                    diffLeft += window[midPoint].getMagnitude() - window[i].getMagnitude();
                for J in range(midPoint, self.windowSize):
                    diffRight += window[midPoint].getMagnitude() - window[J].getMagnitude();
        
                # Calculate the score and append to the output list
                score = (diffRight + diffLeft) / (self.windowSize - 1)
                dp = DataPoint(score, window[midPoint].getTime())
                peakScoreData.append(dp)
                #Pop out the oldest point from the window
                window.pop(0)
            
        #print('scoring stage:', peakScoreData)
        
        return peakScoreData