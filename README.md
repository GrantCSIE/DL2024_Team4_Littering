# DL2024_Team4_Littering
2024 CCU Introduction to deep learning final project

# Dataset
## Information of the dataset
We use a littering dataset, namely, littering-whlsk_dataset from Roboflow Universe:  
https://universe.roboflow.com/thesis-kztn8/littering-whlsk/dataset/8/download/yolov7pytorch,   
which contains 15000 training, 1168 validation, and 1232 testing images.  
Besides, there are some data arguments in the dataset:
1. horizontal flip
2. 30% maximum zoom
3. 15 degrees horizontal shear
4. 15 degrees vertical shear
5. applying 10 percent of images to grayscale
6. limiting hue between -25 degrees and 25 degrees
7. 5 percent of pixels of bounding box are noised.

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


## How to feeding the dataset into the model

After you entered the website from above, choose "download zip to computer" and "continue", and the dataset will be downloaded.  

![image](https://raw.githubusercontent.com/GrantCSIE/DL2024_Team4_Littering/main/Illustrated%20image/dataset%20download.jpg?token=GHSAT0AAAAAACSLZ7HVV5GLW2INIRYGRSBQZSF2JGQ)    

The dataset is named as "Littering.v8-yolotiny.yolov7pytorch". Move it to this repository, and the repository will look like:  
<pre>
<code>
DL2024_Team4_Littering-main
├── __pycache__
├── cfg
├── data
├── ...
├── tools
├── utils
├── Littering.v8-yolotiny.yolov7pytorch (this folder is the downloaded dataset of littering images)
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

Single GPU training   
for NVIDIA RTX 2080 Ti, we highly recommend set the batch size as 1 to prevent OOM.  

<pre>
<code>
python train.py --workers 8 --device 0 --batch-size 1 --data data/data_littering.yaml --img 1920 1080 --epochs 15 --cfg cfg/training/yolov7.yaml --weights '' --name "the name of weight" --hyp data/hyp.scratch.p5.yaml
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
│ ├──  train
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
python detect.py --weights "weight_path" --conf 0.25 --img-size 1920 --source "testing_img_path"
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
│ ├──  detect
│ │ ├── "the name of weight"
│ │ │ ├── exp (the results will located here)  
├── .gitignore
├── detect.py
├── ...
├── train.py
├── train_aux.py
</code>
</pre>
