# Step Counting Model

## Objective
Develop a model that counts walking steps using FlexiTail data. This model is based on 'https://oxford-step-counter.github.io/'

## Content
* `literature review` contains a research paper used as a reference to optimize model parameters.
* `step-counter` contains a python file used to validate a model.
* `optimisation` contains data used to optimize the parameters of a model.


  
## Getting started
    
A statistical model is derived from the Oxford Java step counter algorithm. Please read the references available in the GitHub repository 'https://github.com/Oxford-step-counter/Java-Step-Counter'

Step detection model consists of five steps:

* Pre-processing stage
* Filtering stage
* Scoring stage
* Detection stage
* Post-processing stage
    
For each stage, a separate function is defined. As stated in the reference file the optimal set of parameters is used for step detection.

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Signal%20at%20each%20processing%20stage.png)

**Fig : Signal at each processing stage. The ground truth shows the moment when a step was detected by device.**

    

## Sample Results:

**Wearing `FlexiTail` tight (Acceleration in x-dirextion is >-3000 m/s^2)**

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Wearing%20flexitail%20tight.png)



**Wearing `FlexiTail` loose (Acceleration in x-dirextion is <-3000 m/s^2)**

![image](https://github.com/Swapnil-Rakshe/Swapnil-Rakshe/blob/main/Wearing%20flexitail%20loose.png)

