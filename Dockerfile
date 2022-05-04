FROM ultralytics/yolov5
ADD best.pt /model/best.pt
ADD detect-inputs.sh ./detect-inputs.sh
