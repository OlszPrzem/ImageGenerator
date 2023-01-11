# ImageGenerator

Project prepared as a recruitment task. 

The goal of the program is to create two employees: Producer and Customer, operate in separate threads. The Producer, using sourcemethod is to generate new frames and put them in queue A. 
The Client get frames from queue A, resize their size twice and applies a median filter. The finished image is put to queue B.  
In the main loop of the program, the images from queue B are downloaded and saved in a specified folder.

## Requirements:
```
Python 3.10.8

Package         Version
--------------- ---------
numpy           1.24.1
opencv-python   4.7.0.68
pandas          1.5.2
pytest          7.2.0
pytest-cov      4.0.0
```
