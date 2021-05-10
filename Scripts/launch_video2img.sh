#!/bin/bash

#------------------------------------
echo "Convirtiendo video a una sequencia de frames .png"
#python3 video2img.py ../Datasets/TEST/mav0/cam0/data_video/XiaomiMiA3.mp4 ../Datasets/TEST/mav0/cam0/data/ 30 

python3 video2img.py ../Datasets/TEST_3/mav0/cam0/data_video/XiaomiMiA3.mp4 ../Datasets/TEST_3/mav0/cam0/data/ 20 ../Datasets/TEST_3/mav0/cam0/data.csv