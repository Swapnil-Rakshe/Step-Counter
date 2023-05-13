# Step Counting Model

## Objective
The objective of this project was to create a model capable of accurately counting walking steps using the FlexiTail dataset. The algorithm analysesd the accelerometer signal in order to estimate the number of steps. The FlexiTail dataset consists of accelerometer readings obtained from sensors mounted on the spinal cord. This model is based on 'https://oxford-step-counter.github.io/'

## Content
* `literature review` contains a research paper used as a reference to optimize model parameters.
* `step-counter` contains code files in Jupyter Notebook.
* `optimisation` contains data used to optimize the parameters of a model.
* `src` contains source code.

## Methodology and Dataset
The step counter algorithm used in this project is based on the Windowed Peak Detection method. The dataset utilized in the study comprises measurements obtained from 18 left side sensors and 18 right side sensors, including readings from 3 accelerometers and 3 gyrometers in 3 directions. Additionally, the dataset includes a timestamp value and a constant. 
  
## Getting started
    
A statistical model is derived from the Oxford Java step counter algorithm. 

Step detection model consists of five steps:

* "Pre-processing stage": this stage is responsible for computing the magnitude of the triaxial accelerometry signal and ensuring a constant sampling frequency by means of linear interpolation. 
* "Filtering stage": Accelerometers are subject to noise from a variety of sources (mechanical, electrical, thermal,etc.), therefore some noise-reduction technique is needed especially at frequencies that are not related to human walking or running. In order to reduce the noise level, we have implemented a finite impulse response (FIR) low-pass filter with a cut-off frequency of 3 Hz, which allows a variety of walking speeds. This value should include even the pace of the speediest walkers, which was identified as 5.4 mph (8.7 km/h) by the American College of Sports Medicine, with a ratio of 2000 steps per mile (1250 steps per km). An
example of the raw accelerometer signal after interpolation and filtering is shown in figure.
* "Scoring stage":  The function of the scoring stage is to evaluate the peakiness of a given sample. The result of this stage should increase the magnitude of any peaks, making them more evident for the subsequent peak detection.
* "Detection stage": This stage identifies potential candidate peaks to be associated with a step by statistically detecting outliers. 
* "Post-processing stage": This stage slides a window of a fixed size, across the potential peaks and only keeps the maximum sample within the window. As the small dots in figure show, all of the potential peak points are clustered around the rise to the main peak. This stage selects the local maximum among them.
    
For more details you can visit the following GitHub repository 'https://github.com/Oxford-step-counter/Java-Step-Counter'

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Signal%20at%20each%20processing%20stage.png)

**Fig : Signal at each processing stage. The ground truth shows the moment when a step was detected by device.**

    

## Sample Results:

**Wearing `FlexiTail` tight (Acceleration in x-dirextion is >-3000 m/s^2)**

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Wearing%20flexitail%20tight.png)



**Wearing `FlexiTail` loose (Acceleration in x-dirextion is <-3000 m/s^2)**

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Wearing%20flexitail%20loose.png)

