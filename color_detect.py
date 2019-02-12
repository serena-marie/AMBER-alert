# current implementation only considers red - blue - or green
# how to implement to consider more colors? is CNN the best approach? 
# possible solution: if fall into undefined, approach differently. KNN? 

import numpy as np
import cv2
import glob
import webcolors

#files = glob.glob("data/red_test.png")
files = glob.glob("data/*.png")

for f in files:
  print("Testing......")
  print("File Loaded: ",f)
  img = cv2.imread(f) 
 
  # convert into 1D arr of len 3, BGR 
  BGR = img.reshape((-1,3))

  # convert to RBG
  # RGB = cv2.cvtColor(BGR, cv2.COLOR_BGR2RGB)
  
  # convert to np.float32, need for kmeans function
  BGR = np.float32(BGR)
  # RGB = np.float32(RGB)

  # define criteria for kmeans algorithm
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
  K = 1
  ssd,label,center=cv2.kmeans(BGR,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
  #ssd,label,center=cv2.kmeans(RGB,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

  # print("Value of center is ", center)

  prediction = "n.a"

  # print("Center is ",center)
  # print("RBG is ", RBG)
  # get the max values' y-axis index
  # and categorize color
  index = center.argmax(axis=1)
 
  if index == 0:
     prediction = "Blue"
  elif index == 1:
     prediction = "Green"
  elif index == 2:
     prediction = "Red"
  else:    
     print("Undefined behavior");

  print("Prediction:",prediction)
