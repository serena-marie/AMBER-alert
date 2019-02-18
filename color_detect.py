import numpy as np
import cv2
import glob
import webcolors

files = glob.glob("data/*.png")

for f in files:
  print("\n\nTesting......")
  print("File Loaded: ",f)
  
  # read image
  img = cv2.imread(f) 

  # convert image from BGR to RGB
  img = img[:, :, ::-1]
 
  # convert into 1D arr of len 3, RGB
  # then, convert to np.float32 for kmeans
  RGB = np.float32(img.reshape((-1,3)))

  # define criteria for kmeans algorithm
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
  
  K = 1
  
  ssd,label2,center=cv2.kmeans(RGB,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

  # print("Value of center is ", center)

  prediction = "n.a"

  index = center.argmax(axis=1)
  
  # Determine name of center 
  red = center[0][0]; green = center[0][1]; blue = center[0][2];
  
  if index == 2:
      if((((abs(red-green) < 5) and (abs(green-blue)) < 5) and (300< red+green+blue < 449))):
          prediction = "Silver"
      elif((((abs(red-green) < 20) and (abs(green-blue)) < 20) and (red+green+blue > 450))):
          prediction = "White"
      elif(((abs(red-green) < 10) and (abs(green-blue) < 10)) and (red+green+blue < 300)):
          prediction = "Black"
      else:
          prediction = "Blue"
  elif index == 1:
      prediction = "elif Green"
  elif index == 0:
      if( 8 <= abs(red-green) <= 20):
          prediction = "elif if Yellow" 
      elif(40 <= (abs(red-green)) <= 155):
          prediction= "elif if Orange"
      elif(((abs(red-green) < 10) and (abs(green-blue) < 10)) and (red+green+blue < 300)):
          prediction = "Black"
      elif(red+green+blue >= 450):
          prediction="White"
      else:
          prediction= "Red"
  else:    
     print("Undefined behavior");

  print("Prediction:",prediction)
