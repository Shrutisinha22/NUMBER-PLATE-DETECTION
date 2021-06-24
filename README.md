# NUMBER-PLATE-DETECTION
a module to save images of car License plate from video feed. and another to get the number of the license plate from image feed..


## 1. to save images of car License plate from video feed.

the code file:- 
             
             code.py
                  
                  
**This program plays the video provided to it and using pre-trained model, it identifies car number plate and selectes the area containing the plate as "region-of-interest". Upon pressing the 's' key a screenshot of the license plate is save in the designated folder in an ordered fashion.**

Note: Currently this project works best for russian number plates as the model used here is trained on russian number plates.


### prerequisite:- following libraries are needed to install:

* Python 3
* OpenCV
* Numpy

### sample Output

<img src="https://github.com/Shrutisinha22/NUMBER-PLATE-DETECTION/blob/main/sample%20image.JPG"/>

## 2. to get the number of the plate from image of car.

the code file:- 
             
             untitled-1.ipynb
             

**this  will detect the plate and return the number of the license plate in the figure .**

### prerequisite:- following libraries are needed to install:

* Python 3
* OpenCV
* easyocr   
          
          pip install easyocr
     
      
* imutils

          pip install imutils
          
### sample image for detection - image4.png


### sample Output

<img src="https://github.com/Shrutisinha22/NUMBER-PLATE-DETECTION/blob/main/sampl.JPG"/>
          




