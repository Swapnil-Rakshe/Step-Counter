import pandas as pd
import numpy as np
import math
from datetime import datetime

from src.detection import DetectionStage
from src.preprocessing import PreProcessingStage
from src.filteration import FilterStage
from src.scoring import ScoringStage
from src.postprocessing import PostProcessStage
     





class stepcounter:
    def __init__(self, data_file, samplingperiod=60, SKIPFILTER=False, filterlength=13, filterSTD=0.35, windowSize=35, threshold=1.2, timeThreshold=200):
        self.data_file = data_file
        self.samplingperiod = samplingperiod
        self.SKIPFILTER = SKIPFILTER
        self.filterlength = filterlength
        self.filterSTD = filterSTD
        self.windowSize = windowSize
        self.threshold = threshold
        self.timeThreshold = timeThreshold
        
    def read_data(self):
        '''
         read the csv file present at current path

        Parameters
        ----------
        data_files = list
            list of all data sets
        data : DataFrame
            pandas dataframe contain accelerometer and corr time values 
        sample_time: int
            time for one accelerometer data point
        sampli_frequency : float
            data collection frequency
        threshold:float
            detection threshold. default is 1.2
    
        Returns
        -------
        raw_DF : DataFrame
            pandas dataframe which contains all csv data.
        '''
        data = pd.read_csv(self.data_file, header=None)
        file_name = data.split('_')
        data = data.iloc[:,-8:]
        data.columns = ['acc_x', 'acc_y', 'acc_z','a','b','c','constant', 'time']
        sample_time = int((data['time'][1]) - (data['time'][0])) #calculate actual sampli time
        sample_frequency = float(1/(sample_time * 1e-3)) #calculate actual sampling frequency
        thresholdvalue = float((1.2 * sample_frequency) / 100) #threshold value considering 1.2 is std value for 100Hz
        acc_value = data['acc_x'][0] 
        if acc_value >= -3000:   # Assumed threshold value to compensate tighteness or lossness of flexitail
            skipfilter = True
        else:
            skipfilter = False
        steps, d1 = self.RunAlgo(data,samplingPeriod = sample_time, SKIPFILTER = skipfilter, filterlength = 13, filterSTD = 0.35,  windowSize = 35, threshold = thresholdvalue, timeThreshold = 200)
        
        start_time = datetime.fromtimestamp(int(str(data['time'].iloc[0])[0:-3])).strftime('%Y-%m-%d %H:%M:%S')
        end_time = datetime.fromtimestamp(int(str(data['time'].iloc[-1])[0:-3])).strftime('%H:%M:%S')
        if len(file_name) <= 4:
            print( start_time, end_time, file_name[3], ':', steps)
        else:
            print( start_time, end_time, file_name[4], file_name[6], ':', steps)
        
    # Run algorithm

    def RunAlgo(self) :
    
        '''
    Implement the oxford java step counter algorithm

    Parameters
    ----------
    data : DataFrame
        input data required for preprocessing stage.
    samplingPeriod : float, optional
        Time period to interpolate data points. The default is 60 millisecond.
    SKIPFILTER : bool, optional
        wheather filter stage should be executed or not. The default is False.
    filterLength : int, optional
        length of filter window. The default is 13.
    filterSTD : float, optional
        std dev for generating filter coefficients. The default is 0.35.
    windowSize : int, optional
        length of window in scoring stage. The default is 35.
    threshold : float, optional
        threshold required for detection stage. The default is 1.2.
    timeThreshold : float/int, optional
        time in millisecond, used to detect steps. The default is 200.

    Returns
    -------
    steps : int
        number of steps.
    detectedStepsList : list
        datapoints for which step is detected.

    '''
    
        ppData = PreProcessingStage(self.data)

        if (not self.SKIPFILTER):
            smoothData = self.FilterStage(ppData)
        else:
            smoothData = ppData
        peakScoreData = ScoringStage(smoothData, self.windowSize)
        peakData = DetectionStage(peakScoreData, self.threshold)
        steps, detectedStepsList = PostProcessStage(peakData, self.timeThreshold)
        return steps, detectedStepsList
    
    
if __name__=="__main__":
    counter = stepcounter(data_file = "optimisation\1663927235497_Max_walking_5hz-50steps.csv")
    