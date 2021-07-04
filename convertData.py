# This script converts from Yolov5 (ultralytics) format to UCF-QNRF_ECCV18 format.
# 

import os
import cv2
import argparse
import scipy.io

my_parser = argparse.ArgumentParser(description='Plot the QNRF data to check it')
my_parser.add_argument('--yolopath', default="./yoloDataset/",
                    help='the path to the input yolo format data, folder should contain images and labels dirs')
my_parser.add_argument('--qnrfpath', default="./QNRFDataset/",
                    help='the output path where QNRF format data will be written to')

args = my_parser.parse_args()

if os.path.isdir(args.qnrfpath):
    raise FileExistsError('The output path already exists!')