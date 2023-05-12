import pandas as pd
from datetime import datetime

from detection import detection
from preprocessing import preprocessing
from filteration import filteration
from scoring import scoring
from postprocessing import postprocessing
     
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
     
        data_1 = pd.read_csv(self.data_file, header=None)
        file_name = self.data_file.split('_')
        data_1 = data_1.iloc[:,-8:]
        data_1.columns = ['acc_x', 'acc_y', 'acc_z','a','b','c','constant', 'time']
        sample_time = int((data_1['time'][1]) - (data_1['time'][0])) #calculate actual sampli time
        sample_frequency = float(1/(sample_time * 1e-3)) #calculate actual sampling frequency
        thresholdvalue = float((1.2 * sample_frequency) / 100) #threshold value considering 1.2 is std value for 100Hz
        acc_value = data_1['acc_x'][0] 
        if acc_value >= -3000:   # Assumed threshold value to compensate tighteness or lossness of flexitail
            skipfilter = True
        else:
            skipfilter = False
        steps, d1 = self.RunAlgo(data = data_1,samplingPeriod = sample_time, SKIPFILTER = skipfilter, filterlength = 13, filterSTD = 0.35,  windowSize = 35, threshold = thresholdvalue, timeThreshold = 200)
        
        start_time = datetime.fromtimestamp(int(str(data_1['time'].iloc[0])[0:-3])).strftime('%Y-%m-%d %H:%M:%S')
        end_time = datetime.fromtimestamp(int(str(data_1['time'].iloc[-1])[0:-3])).strftime('%H:%M:%S')
        if len(file_name) <= 4:
            print( start_time, end_time, file_name[3], ':', steps)
        else:
            print( start_time, end_time, file_name[4], file_name[6], ':', steps)
        
    # Run algorithm

    def RunAlgo(self,data, samplingPeriod, SKIPFILTER, filterlength, filterSTD, windowSize, threshold, timeThreshold) :
        pp = preprocessing()
        ppData = pp.PreProcessingStage(data = data)

        if (not self.SKIPFILTER):
            filter = filteration()
            smoothData = filter.FilterStage(ppData)
        else:
            smoothData = ppData
        score = scoring()
        peakScoreData = score.ScoringStage(smoothData, windowSize)
        detect = detection()
        peakData = detect.DetectionStage(peakScoreData, threshold)
        postprocess = postprocessing()
        steps, detectedStepsList = postprocess.PostProcessStage(peakData, timeThreshold)
        return steps, detectedStepsList
    
    
if __name__=="__main__":
    counter = stepcounter(data_file="optimisation/1663926837642_Max_walking_15hz-50steps.csv")
    counter.read_data()
    