#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import libraries
import cv2
import numpy as np


# In[12]:


#captures frames from a camera
camera =cv2.VideoCapture(0)


# In[ ]:


#loops runs if capturing has been initialized
while True:
    _, frame=camera.read()
    cv2.imshow('Camera',frame)
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    laplacian=np.uint8(laplacian)
    cv2.imshow('Laplacian',laplacian)
    edges=cv2.Canny(frame,100,100)
    cv2.imshow('Canny',edges)
    
    
    #wait for Esc key to stop
    if cv2.waitKey(5)==ord('x'):
        break
#close the window
camera.release()

#de-allocate any associated memory usage
cv2.destoryAllWindows()


# In[ ]:




