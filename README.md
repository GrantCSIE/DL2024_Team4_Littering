# DL2024_Team4_Littering
2024 CCU Introduction to deep learning final project

# Dataset
## Information of the dataset
We use some datasets
1. m0t0rcycl3 from Roboflow Universe:  
  [https://universe.roboflow.com/thesis-kztn8/littering-whlsk/dataset/8/download/yolov7pytorch](https://universe.roboflow.com/tip-m0-0r/m0t0rcycl3/dataset/2),   
  which contains 4908 training, 751 validation, and 764 testing images.
2. Trash Bag Detector Image from Roboflow Universe:  
   [https://universe.roboflow.com/thesis-kztn8/littering-whlsk/dataset/8/download/yolov7pytorch](https://universe.roboflow.com/tip-m0-0r/m0t0rcycl3/dataset/2),  
  which contains 13988 training, 1998 validation, and 999 testing images.


## Download weights
Step 1: Download our best weights:  
[best garbage model](https://drive.google.com/file/d/1tE0HEUrhzbZ0iKt_7t802HDco0RD_AP7/view?usp=sharing)  
[best scooter model](https://drive.google.com/file/d/15-5UNSwIoHjSbdX1A_6vFiHGLfuN9Bud/view?usp=sharing)  
Step 2: Move the weights into the root folder of repository.

## Dataset Structure

### training set
<pre>
<code>  
├── images  
│ ├── video_1_1_jpg.rf.0be38e966cef7fc7471a0a8bffa7b1eb.jpg
│ ├── video_1_1_jpg.rf.1cf33b16b1319e73fdc5789d42186e18.jpg
│ ├── ...  
│ ├── video_1_2_jpg.rf.1cce7cbaa210f71ba05dae70e307bbfd.jpg
│ ├── video_1_2_jpg.rf.2ccc58c4e2cd3eeec7bb39e9efa7ffe6.jpg
│ ├── ...  
│ ├── video_12_30_jpg.rf.2e1837fe76a3b97ebf35c10adf25c206.jpg
│ ├── video_12_30_jpg.rf.3a489ff20cfa47f030001235ff86da24.jpg
├── label
│ ├── video_1_1_jpg.rf.0be38e966cef7fc7471a0a8bffa7b1eb.txt
│ ├── video_1_1_jpg.rf.1cf33b16b1319e73fdc5789d42186e18.txt
│ ├── ...  
│ ├── video_1_2_jpg.rf.1cce7cbaa210f71ba05dae70e307bbfd.txt
│ ├── video_1_2_jpg.rf.2ccc58c4e2cd3eeec7bb39e9efa7ffe6.txt
│ ├── ...  
│ ├── video_12_30_jpg.rf.2e1837fe76a3b97ebf35c10adf25c206.txt
│ ├── video_12_30_jpg.rf.3a489ff20cfa47f030001235ff86da24.txt
</code>
</pre>

### validation set
<pre>
<code>  
├── images  
│ ├── video_1_1_jpg.rf.2a8c7343fe6c5aa59f2a28a18cd5b839.jpg
│ ├── video_1_1_jpg.rf.42a3806529c18b21d191131c870f3f1c.jpg
│ ├── ...  
│ ├── video_1_2_jpg.rf.0dae2585dff931fda058f0a35a5fc799.jpg
│ ├── video_1_2_jpg.rf.33a1c11df69bc12e487941dda5c124f0.jpg
│ ├── ...  
│ ├── video_12_30_jpg.rf.0669bfff657d45c74b047082cf4609c0.jpg
│ ├── video_12_30_jpg.rf.d6f9012b09117f369dddae9544af880b.jpg
├── label
│ ├── video_1_1_jpg.rf.2a8c7343fe6c5aa59f2a28a18cd5b839.txt
│ ├── video_1_1_jpg.rf.42a3806529c18b21d191131c870f3f1c.txt
│ ├── ...  
│ ├── video_1_2_jpg.rf.0dae2585dff931fda058f0a35a5fc799.txt
│ ├── video_1_2_jpg.rf.33a1c11df69bc12e487941dda5c124f0.txt
│ ├── ...  
│ ├── video_12_30_jpg.rf.0669bfff657d45c74b047082cf4609c0.txt
│ ├── video_12_30_jpg.rf.d6f9012b09117f369dddae9544af880b.txt
</code>
</pre>

### testing set
<pre>
<code>  
├── images  
│ ├── video_1_1_jpg.rf.1f706338279dea3181448a9ed38e7877.jpg
│ ├── video_1_1_jpg.rf.4e3d07b524f1aa7437a590d9d071b84e.jpg
│ ├── ...  
│ ├── video_1_2_jpg.rf.2ff9c29d7422a923d01288a9e1e408d3.jpg
│ ├── video_1_2_jpg.rf.3c7acbb79d30a223d889ff82f610bcc0.jpg
│ ├── ...  
│ ├── video_12_30_jpg.rf.6cb9b92867c9cc3bd587ab5664052674.jpg
│ ├── video_12_30_jpg.rf.3767ab8996dfbd4d8b25902b98ada7b4.jpg
├── label
│ ├── video_1_1_jpg.rf.1f706338279dea3181448a9ed38e7877.txt
│ ├── video_1_1_jpg.rf.4e3d07b524f1aa7437a590d9d071b84e.txt
│ ├── ...  
│ ├── video_1_2_jpg.rf.2ff9c29d7422a923d01288a9e1e408d3.txt
│ ├── video_1_2_jpg.rf.3c7acbb79d30a223d889ff82f610bcc0.txt
│ ├── ...  
│ ├── video_12_30_jpg.rf.6cb9b92867c9cc3bd587ab5664052674.txt
│ ├── video_12_30_jpg.rf.3767ab8996dfbd4d8b25902b98ada7b4.txt
</code>
</pre>


## How to feed the dataset into the model

After you enter the website from above, choose "download zip to computer" and "continue", and the dataset will be downloaded.  

Rename the folder of first and second datasets as "dataset_scooter" and "dataset_garbage", respectively.  
  
Move them to this repository, and the repository will look like:  
<pre>
<code>
DL2024_Team4_Littering-main
├── __pycache__
├── cfg
├── data
├── ...
├── tools
├── utils
├── dataset_scooter (this folder is the downloaded dataset of images containing scooters)
├── dataset_garbage (this folder is the downloaded dataset of images containing garbage bags)
├── .gitignore
├── detect.py
├── ...
├── train.py
├── train_aux.py
</code>
</pre>

# Model
The project is employed a state-of-the-art model, namely, you only look once v7(YOLOv7):  
https://github.com/WongKinYiu/yolov7?tab=readme-ov-file  
Recently, it has the best performance in COCO dataset:  
![image](https://raw.githubusercontent.com/WongKinYiu/yolov7/main/figure/performance.png)  



# Training
Change the dictionary
<pre>
<code>
cd "YOLOv7_path"
</code>
</pre>

Single GPU training for training the model with garbage dataset (we will call it as garbage model later).  
for NVIDIA RTX 2080 Ti, we highly recommend set the batch size as 1 to prevent OOM.  

<pre>
<code>
python train.py --workers 8 --device 0 --batch-size 1 --data data/data_garbage.yaml --img 640 640 --epochs 50 --cfg cfg/training/yolov7.yaml --weights 'path of pretrained model' --name "the name of weight" --hyp data/hyp.scratch.p5.yaml # this is training the model which detect the garbage bags 
</code>
</pre>   

Single GPU training for training the model with scooter dataset (we will call it as scooter model later).  
for NVIDIA RTX 2080 Ti, we highly recommend set the batch size as 1 to prevent OOM.  

<pre>
<code>
python train.py --workers 8 --device 0 --batch-size 1 --data data/data_scooter.yaml --img 640 640 --epochs 50 --cfg cfg/training/yolov7.yaml --weights 'path of pretrained model' --name "the name of weight" --hyp data/hyp.scratch.p5.yaml # this is training the model which detect the scooters (scooter model)
</code>
</pre>   
After finishing to train the model, the weight will be located at:

<pre>
<code>
DL2024_Team4_Littering-main
├── __pycache__
├── cfg
├── data
├── ...
├── runs
│ ├── train
│ │ ├── "the name of weight"
│ │ │ ├── weights
│ │ │ │ ├── best.pt (this is the best weight of the model)
│ │ │ │ ├── epoch_000.pt
│ │ │ │ ├── epoch_010.pt
│ │ │ │ ├── ...
│ │ │ │ ├── init.pt
│ │ │ │ ├── last.pt
│ │ │ ├── confusion_matrix.png
│ │ │ ├── ...
│ │ │ ├── train_batch9.jpg
├── .gitignore
├── detect.py
├── ...
├── train.py
├── train_aux.py
</code>
</pre>

# Testing
<pre>
<code>
python detect.py --weights "weight_path" --conf 0.25 --img-size 1280 --source "testing_img_path" --save-txt
</code>
</pre>

After testing with custom images or video, the results will be located at:

<pre>
<code>
DL2024_Team4_Littering-main
├── __pycache__
├── cfg
├── data
├── ...
├── runs
│ ├── detect
│ │ ├── "the name of weight"
│ │ │ ├── exp (the results will located here)
│ │ │ │ ├── labels
│ │ │ │ ├── *.mp4
├── .gitignore
├── detect.py
├── ...
├── train.py
├── train_aux.py
</code>
</pre>

# Detect littering

If you are using the "scooter Model" to detect the body of scooter in the video, move "labels" folder in "exp" folder to "exp_motor" in "detect_label" folder,
otherwise, move "labels" folder in "exp" folder to "exp_garbage" in "detect_label" folder.

<pre>
<code>
DL2024_Team4_Littering-main
├── __pycache__
├── cfg
├── data
├── ...
├── runs
├── detect_label
│ ├── exp_motor
│ ├── exp_garbage
│ ├── find_littering.py
├── .gitignore
├── detect.py
├── ...
├── train.py
├── train_aux.py
</code>
</pre>

After that, execute find_littering.py in "detect_label" folder or executing:
<pre>
<code>
python ./detect_label/find_littering.py
</code>
</pre>
The result will be shown on command prompt like this:
![image](https://github.com/GrantCSIE/DL2024_Team4_Littering/blob/master/result.jpg)
