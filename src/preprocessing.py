from utils import DataPoint

class preprocessing:
    def __init__(self):
        pass
    
    def PreProcessingStage(self,data):
         
        ppData = []  # List to append the the return value of class data point i.e Datapoint 1 - Magnitude and corr time
        DataLen = len(data["time"]) # total number of data points in the data set
        for i in range(DataLen):
            acc_mag = ((data["acc_x"][i] ** 2 + data["acc_y"][i] ** 2 + data["acc_z"][i] **2)** 0.5) # acceleration magnitude
            cur_time = data["time"][i]
            dp = DataPoint(mag = acc_mag, time = cur_time)
            ppData.append(dp)
        #print('preprocessing stage:', ppData)
        return ppData        