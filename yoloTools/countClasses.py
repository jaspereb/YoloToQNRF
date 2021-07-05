# -*- coding: utf-8 -*-

import os
from os import walk, getcwd
import numpy as np
import cv2
    
"""-------------------------------------------------------------------""" 

""" Configure Paths"""   
mypath = "./dataset/"

objectCount = {}

wd = getcwd()

""" Get yolo txt file list """
txt_list = []
for file in sorted(os.listdir(mypath)):
    if file.endswith(".txt"):
        txt_list.append(file)
    

""" Process """
for txt_name in txt_list:
    """ Open input text files """
    txt_path = mypath + txt_name
    txt_file = open(txt_path, "r")

    lines = txt_file.read().splitlines()  
    for idx, line in enumerate(lines):
        value = line.split()
        cls = value[0]
        assert(cls.isdigit())

        if(objectCount.get(cls) is None):
            objectCount[cls] = 1
        else:
            objectCount[cls] = int(objectCount[cls] + 1)
	
print("Read {} annotation files \n".format(len(txt_list)))

print("Found the following number of objects annotated:\n")
for cls in objectCount:
    print("{} objects of class {}".format(objectCount[cls], cls))
