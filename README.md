# DL2024_Team4_Littering
2024 CCU Introduction to deep learning final project

# Dataset
We use a littering dataset, namely, littering-whlsk_dataset from Roboflow Universe:  
https://universe.roboflow.com/thesis-kztn8/littering-whlsk  
, which contains 15000 training, 1168 validation, 1232 testing images.  
Besides, there are some data arguments in the dataset including horizontal flip, 30% maximum zoom, 15 degrees horizontal   shear,  15 degrees vertical shear, applying 10 percent of images to grayscale, limiting hue between -25 degrees to 25 degrees,   and 5 percent of pixels of bounding box are noised.

# Model
The project is employed a state-of-the-art model, namely, you only look once v7(YOLOv7):  
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
<code>
python detect.py --weights runs/train/v7_0514/weights/best.pt --conf 0.25 --img-size 1920 --source "testing_img_dictionary"
</code>

# Dataset Structure

## Train Directory Structure

### Images

<pre>
<code>
train  
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
  
valid
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
test
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
