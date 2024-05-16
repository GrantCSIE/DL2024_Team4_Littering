# DL2024_Team4_Littering
2024 CCU Introduction to deep learning final project

# Dataset
We use a littering dataset, namely, littering-whlsk_dataset from Roboflow Universe:
https://universe.roboflow.com/thesis-kztn8/littering-whlsk
, which contains 15000 training, 1168 validation, 1232 testing images.
Besides, there are some data arguments in the dataset including horizontal flip, 30% maximum zoom, 15 degrees horizontal shear,  15 degrees vertical shear, applying 10 percent of images to grayscale, limiting hue between -25 degrees to 25 degrees, and 5 percent of pixels of bounding box are noised.

# Model
The project is employed a state-of-a-art model, namely, you only look once v7(YOLOv7):
https://github.com/WongKinYiu/yolov7?tab=readme-ov-file
Recently, it has the best performance in COCO dataset:
![image](https://raw.githubusercontent.com/WongKinYiu/yolov7/main/figure/performance.png)

