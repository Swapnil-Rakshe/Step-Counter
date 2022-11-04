# Step Counting Algorithm

## Objective
Develop an algorithm that counts the walking steps using `FlexiTail` data. This algorith is based on 'https://oxford-step-counter.github.io/'

## Content
* `optimisation` contains data used to optimize the parameters of the algorithm
* `step-counter` contains python file used to validate the algorithm
* `Literature review` contain research paper used as a refrence to optimize the parameters of the algorithm

  
## Getting started
    
The python algorithm is derived from oxford java step counter algorithm. Please read the references available in github repository 'https://github.com/Oxford-step-counter/Java-Step-Counter'

Step detection algorithm consist of five steps:

* Pre-processing stage
* Filtering stage
* Scoring stage
* Detection stage
* Post-processing stage
    
For each stage a separate function is defined. As stated in the reference file the optimal set of parameters are used for the step detection.

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Signal%20at%20each%20processing%20stage.png)

**Fig : Signal at each processing stage. The ground truth shows the moment when a step was detected by device.**

    

## Sample Results:

**Wearing `FlexiTail` tight (Acceleration in x-dirextion is >-3000 m/s^2)**

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Wearing%20flexitail%20tight.png)



**Wearing `FlexiTail` loose (Acceleration in x-dirextion is <-3000 m/s^2)**

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Wearing%20flexitail%20loose.png)

