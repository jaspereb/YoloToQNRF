# This script converts from Yolov5 (ultralytics) format to UCF-QNRF_ECCV18 format.
# Basically read each bounding box, take the centroid, convert to pixel coords and write this to a matlab array.
# Then save the image, and annotation .mat to the correct locations

import os
import cv2
import argparse
import scipy.io
import numpy as np
from shutil import copyfile

my_parser = argparse.ArgumentParser(description='Convert Yolov5 format data to QNRF format')
my_parser.add_argument('--yolopath', default="./yoloDataset/",
                    help='the path to the input yolo format data, folder should contain images and labels dirs')
my_parser.add_argument('--qnrfpath', default="./QNRFDataset/",
                    help='the output path where QNRF format data will be written to')
my_parser.add_argument('--structinfopath', default="./structInfo.mat",
                    help='the location of the structInfo.mat file')
my_parser.add_argument('--classnum', default=0, type=int,
                    help='(int) the class type number to count as annotations')
my_parser.add_argument('--startcount', default=1, type=int,
                    help='(int) the number to start file naming from, handy if combining datasets')

args = my_parser.parse_args()

# structInfo = scipy.io.loadmat(args.structinfopath)

if os.path.isdir(args.qnrfpath):
    assert(len(os.listdir(args.qnrfpath))<2) #The output dir must be empty (can contain .gitkeep)
os.makedirs(os.path.join(args.qnrfpath,'Test'))
os.makedirs(os.path.join(args.qnrfpath,'Train'))

labelsDirs = os.listdir(os.path.join(args.yolopath, 'labels'))
masterCount = args.startcount
renameList = open(os.path.join(args.qnrfpath,'renamed_files.txt'),'x')

for subdir in labelsDirs: #for train,test,val,... dirs
    labels = sorted(os.listdir(os.path.join(args.yolopath, 'labels', subdir)))
    for label in labels: #For each label .txt file
        if(not os.path.splitext(label)[1] == '.txt'):
            print("Unrecognised file: {}".format(os.path.join(args.yolopath, 'labels', subdir,label)))
            continue

        labelFile = open(os.path.join(args.yolopath, 'labels', subdir,label), 'r')
        imagePath = os.path.join(args.yolopath, 'images', subdir, os.path.splitext(label)[0]+'.JPG')
        I = cv2.imread(imagePath)

        if(I is None):
            print("Failed to read image at {}, skipping".format(imagePath))
            continue

        if(subdir.lower() == 'test'): #the test data goes into test folder
            labelFilePath = os.path.join(args.qnrfpath, 'Test', "img_{:0>4d}_ann.mat".format(masterCount))
            imageFilePath = os.path.join(args.qnrfpath, 'Test', "img_{:0>4d}.jpg".format(masterCount))
        else: #everything else goes into train
            labelFilePath = os.path.join(args.qnrfpath, 'Train', "img_{:0>4d}_ann.mat".format(masterCount))
            imageFilePath = os.path.join(args.qnrfpath, 'Train', "img_{:0>4d}.jpg".format(masterCount))

        mat = []
        for ln in labelFile:

            ann = ln.split()

            if(not args.classnum == int(ann[0])):
                continue
            
            xmid = float(ann[1])*I.shape[1] #From normalised to px coords
            ymid = float(ann[2])*I.shape[0]

            mat.append((xmid,ymid))

        mat = np.array(mat)

        if(mat.shape[0] == 0):
            print("Skipping file with no annotations: {}".format(os.path.join(args.yolopath, 'labels', subdir,label)))
            continue

        mat = {"annPoints": mat}

        #Finally, write both the image and annotation
        scipy.io.savemat(labelFilePath, mat)
        copyfile(imagePath,imageFilePath)
        renameList.write("File {} in yolo renamed to {} in QNRF\n".format(imagePath,imageFilePath))
        masterCount = masterCount + 1


renameList.close()
print("Add done")
