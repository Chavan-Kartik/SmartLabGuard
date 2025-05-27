# Lab Object Detector

This project uses YOLOv8 (Ultralytics) and OpenCV to detect lab equipment : keyboards and mice in a live webcam feed.

Basic idea behind the project is to implement this in a Computer Based Lab where, the camera can be placed in a position where it can capture the entire lab. The system can then detect the presence of keyboards and mice in that particular area.

If there happens a theft or an object is missing, It will be shown in the screen.

Currently 5 keyboard and 5 mice are alloted in the required area, you can change the number of objects in the code "detect_lab_equipment.py" as per your requirement.

## Requirements
- Python 3.8+
- OpenCV
- Ultralytics (YOLOv8)

## Run
```bash
python detect_lab_equipment.py
