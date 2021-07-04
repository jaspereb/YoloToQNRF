# This script plots the QNRF dataset for checking.
# It will search the dataToPlot folder for img_nnnn_ann.mat files then try to find a matching img_nnnn.jpg file and plot the 
# annotations on this image. The image is then saved to the dataPlotted folder. 

import os
import cv2
import argparse
import scipy.io

my_parser = argparse.ArgumentParser(description='Plot the QNRF data to check it')
my_parser.add_argument('--inputpath', default="./dataToPlot/",
                    help='the path to the QNRF data, can be pointed to the UCF-QNRF_ECCV18/Train or Test dir')
my_parser.add_argument('--outputpath', default="./dataPlotted/",
                    help='the output path where images will be written to')
my_parser.add_argument('--circlerad', default=0.004, type=float,
                    help='(float) radius of the circles to plot as image fraction (0-1), default is 0.004')
my_parser.add_argument('--r', default=255, type=int,
                    help='(int) red component of circle colour (0-255)')
my_parser.add_argument('--g', default=0, type=int,
                    help='(int) green component of circle colour (0-255)')
my_parser.add_argument('--b', default=0, type=int,
                    help='(int) blue component of circle colour (0-255)')

args = my_parser.parse_args()


inFiles = sorted(os.listdir(args.inputpath))

for i,file in enumerate(inFiles):
    if(not file.endswith('.mat')):
        continue

    if(not os.path.splitext(file)[0][-4:] == '_ann'):
        print("Skipping .mat file missing _ann postfix: {}".format(file))
        continue

    #find img file
    imName = os.path.splitext(file)[0]
    imName = imName[:-4] + '.jpg'

    try:
        I = cv2.imread(os.path.join(args.inputpath,imName))
    except:
        print("Failed to read image {}, does it exist?".format(imName))

    #read GT
    gtMat = scipy.io.loadmat(os.path.join(args.inputpath,file))
    gtMat = gtMat['annPoints'] #nx2 array
    numberDots = gtMat.shape[0]

    for n in range(0,numberDots):
        radius = int(args.circlerad*I.shape[0])
        I = cv2.circle(I, (int(gtMat[n][0]),int(gtMat[n][1])), radius, (args.b,args.g,args.r), -1) #-1 fills it

    cv2.imwrite(os.path.join(args.outputpath,'plotted_'+imName),I)

    if(i%50 == 0):
        print("Processed {} files".format(i))
   
print("All Done")