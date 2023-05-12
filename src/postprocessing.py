from utils import DataPoint

class postprocessing:
    def __init__(self):
        pass
    

    def PostProcessStage(self, peakData, timeThreshold = 200):
        '''
    Fifth Stage of Step Counting
    ----------------------------
        handles false positives from the detection stage by having a sliding 
        window of fixed size t_window and selecting the higher peak within the window

    Parameters
    ----------
    peakData : list
        this list is output of detection stage.
    timeThreshold : float/int, optional
        The default is 200. Time in millisecond
        By considerng human can walk max 5 steps in a sec.

    Returns
    -------
    steps : int
        number of steps detected by algorithm
    outputQueue : list
        list of datapoints for which step is detected.
    
        '''
    
    
        steps = 0 # number of steps detected
        inputQueue = peakData[:]
        outputQueue = []
        current = peakData[0]
        active = True
        while(active):
            dp = inputQueue.pop(0)
            if(len(inputQueue) == 0):
                active = False
                # dp = DataPoint(0, 0)
                # End of stage
                # continue
        
            if ((dp.getTime() - current.getTime()) > timeThreshold):
                # If the time difference exceeds the threshold, we have a confirmed step
                current = dp
                steps += 1
                outputQueue.append(dp)
            else:
                if (dp.getMagnitude() > current.getMagnitude()):
                    # Keep the point with the largest magnitude.
                    current = dp
    
        return steps, outputQueue