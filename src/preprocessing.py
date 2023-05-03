import pandas as pd
import numpy as np
import math
from datetime import datetime

from utils import DataPoint

class preprocessing:
    def __init__(self, data, samplingPeriod = 60):
        self.data = data
        self.samplingPeriod = samplingPeriod
    
    def PreProcessingStage(self):
        '''
        First stage of step counting
        -----------------------------
            This stage is responsible for computing the magnitude of the triaxial accelerometer signal
            ensuring a constant sampling frequency by means of linear interpolation.

        Parameters
        ----------
        data : DataFrame
            pandas dataframe containing accelerometer values viz. acc_x, acc_y, acc_z 
            and corresponding unix-timestamp
        samplingPeriod : float, optional
            The default is 60.
            sampling period is in milli second (15 Hz) to interpolate values

        Returns
        -------
        ppData : list
            the output list  of preprocessing stage which contains DataPoints.
        '''    
        ppData = []  # List to append the the return value of class data point i.e Datapoint 1 - Magnitude and corr time
        DataLen = len(self.data["time"]) # total number of data points in the data set
        for i in range(DataLen):
            acc_mag = ((self.data["acc_x"][i] ** 2 + self.data["acc_y"][i] ** 2 + self.data["acc_z"][i] **2)** 0.5) # acceleration magnitude
            cur_time = self.data["time"][i]
            dp = DataPoint(acc_mag, cur_time)
            ppData.append(dp)
        #print('preprocessing stage:', ppData)
        return ppData        