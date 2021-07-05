#This splits the qnrfcows.txt file into qnrfcows_train.txt and qnrfcows_val.txt

import argparse
import os

my_parser = argparse.ArgumentParser(description='splits the qnrfcows.txt file into qnrfcows_train.txt and qnrfcows_val.txt')
my_parser.add_argument('--trainpath', default="./QNRFDataset/Train",
                    help='the path to QNRFDataset/Train') 
my_parser.add_argument('--trainfile', default="./QNRFDataset/qnrfcows_train.txt",
                    help='where to write the new train split file')
my_parser.add_argument('--valfile', default="./QNRFDataset/qnrfcows_val.txt",
                    help='where to write the new val split file')
my_parser.add_argument('--samplerate', default=8, type=int,
                    help='(int) One in n files will be moved from train to val')
args = my_parser.parse_args()

# cows = open(args.trainpath,'r')
train = open(args.trainfile, 'x')
val = open(args.valfile, 'x')

imgs = sorted(os.listdir(args.trainpath))

i = 0
for img in imgs:
    if(not os.path.splitext(img)[1] == '.jpg'):
        continue

    if(i%args.samplerate == 0):
        val.write(img+'\n')
    else:
        train.write(img+'\n')

    i = i + 1

train.close()
val.close()


print("Done")