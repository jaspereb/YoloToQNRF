# YoloToQNRF
Convert Yolov5 (ultralytics) format dataset into the UCF-QNRF dataset format (crowd counting) and plot UCF-QNRF format data.

# Installing
Requirements are pretty minimal. 

`cd ~/git/YoloToQNRF` (or wherever this repo is cloned to)

`python3 -m venv ./venv`

`source venv/bin/activate`

`pip3 install requirements.txt`

## Plotting Data
Use the `plotData.py` script to check your annotations. To run this on the QNRF data, copy all the img_nnnn.jpg files you want to check, along with their img_nnnn_ann.mat files directly into the `dataToPlot` directory (no folders below this). Any annotations found in that folder will be plotted to their matching image and saved to `dataPlotted`. The annotations must end with `_ann` and be .mat files with the exact same matlab struct format as the QNRF ones (it's complicated). 

Takes no args, but settings are at the top of the script.

`python3 plotData.py`

## Converting Data

The yolo directory can contain an arbitrary number of folders under 'images' and 'labels' which correspond to dataset splits. Any folder called 'test' in the yolo data, will be put into the QNRF 'Test' dir, everything else will go into 'Train'. 

You can set the yolo class to export using the classnum arg, eg `--classnum 0` and only the first class will be added to the QNRF annotations. You can only export 1 class per dataset.

Either run it from within the repo directory (because it loads the .mat file header from structInfo.mat) or provide the full file path with the `--structinfopath` arg.