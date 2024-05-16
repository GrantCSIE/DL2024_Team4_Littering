# DL2024_Team4_Littering
2024 CCU Introduction to deep learning final project

# Dataset
We use a littering dataset, namely, littering-whlsk_dataset from Roboflow Universe:  
https://universe.roboflow.com/thesis-kztn8/littering-whlsk  
, which contains 15000 training, 1168 validation, 1232 testing images.  
Besides, there are some data arguments in the dataset including horizontal flip, 30% maximum zoom, 15 degrees horizontal   shear,  15 degrees vertical shear, applying 10 percent of images to grayscale, limiting hue between -25 degrees to 25 degrees,   and 5 percent of pixels of bounding box are noised.

# Model
The project is employed a state-of-a-art model, namely, you only look once v7(YOLOv7):  
https://github.com/WongKinYiu/yolov7?tab=readme-ov-file  
Recently, it has the best performance in COCO dataset:  
![image](https://raw.githubusercontent.com/WongKinYiu/yolov7/main/figure/performance.png)  



# Training
Change the dictionary
<pre>
<code>
cd "YOLOv7_dictionary"
</code>
</pre>

Single GPU training
<pre>
<code>
python train.py --workers 8 --device 0 --batch-size 1 --data data/data_littering.yaml --img 1920 1080 --epochs 15 --cfg cfg/training/yolov7.yaml --weights 'test' --name v7_0514 --hyp data/hyp.scratch.p5.yaml
</code>
</pre>

Testing
<pre>
<code>
python detect.py --weights runs/train/v7_0514/weights/best.pt --conf 0.25 --img-size 1920 --source "testing_img_dictionary"
</code>
</pre>

# Dataset Structure

## Train Directory Structure

### Images

<script>
train  
├── images  
│ ├── 0902_150000_151900 (Timestamp: Date_StartTime_EndTime)  
│ │ ├── 0_00001.jpg (CamID_FrameNum)  
│ │ ├── 0_00002.jpg  
│ │ ├── ...  
│ │ ├── 1_00001.jpg (CamID_FrameNum)  
│ │ ├── 1_00002.jpg  
│ │ ├── ...  
│ │ ├── 7_00001.jpg (CamID_FrameNum)  
│ │ ├── 7_00002.jpg  
│ ├── 0902_190000_191900 (Timestamp: Date_StartTime_EndTime)  
│ │ ├── 0_00001.jpg (CamID_FrameNum)  
│ │ ├── 0_00002.jpg  
│ │ ├── ...  
│ │ ├── 1_00001.jpg (CamID_FrameNum)  
│ │ ├── 1_00002.jpg  
</script>
