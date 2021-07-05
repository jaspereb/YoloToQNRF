# yoloTools
This folder is a fork of `https://github.com/ivder/YoloBBoxChecker` which has a script to plot all the bounding boxes and one to count the classes.

Program to extract value from YOLO format data text file and draw a bounding box to clean images. This is the reversed version of common Bounding Box labelling tool whereas this program will draw a bounding box from YOLO dataset (clean image + text file). 

# Purpose
What if somebody annotates the dataset and you want to check whether they draw the bounding box correctly or not?

YOLO only accepts a clean image with its bounding box information stored in text file. 

Use this program to check whether the bounding box is drawn correctly or not during data annotation. It will read the image and text file and convert the value to produce **xmin,ymin,xmax,ymax** of the bounding box and draw it to the images.

# checkBoundingBoxes Usage 
 - Store the dataset (images and text files) to **dataset/** folder
 
 - run `python3 checkBoundingBoxes.py` (OpenCV and Numpy is needed)
 - The result of images with the drawn bounding boxes will be stored in **result/** folder

# countClasses Usage 
 - Set the `mypath` variable at the top of the script or copy the annotations (.txt) files into **dataset/**
 - run `python3 countClasses.py`

# Example
Yolo format data text file + Clean Image dataset
```
0 0.3421875 0.561111111111 0.034375 0.114814814815
0 0.417708333333 0.609259259259 0.0395833333333 0.0740740740741
```
