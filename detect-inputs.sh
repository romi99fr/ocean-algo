#!/bin/bash

unzip -j data/inputs/$DIDS/*.zip -d data/input/ #UNZIP INPUT DATA to /data/input/

wait

python3 detect.py --source data/input # run yolov5 python to detect images at /data/input

wait

cd runs/detect/ # Change workdir

wait

zip -r results.zip exp*/* # Zip the results

wait

mv results.zip ../../data/outputs/. # Move results to /data/outputs/. to get them uploaded

wait
