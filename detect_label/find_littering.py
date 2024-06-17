def detect_littering(susp_cache):
    sum_diff = []
    #紀錄前一次垃圾和機車很近的距離跟這一次垃圾和機車很近的距離的差異
    for i in range(1, len(susp_cache)):
        sum_diff.append(abs(susp_cache[i - 1]['scooter_pos'][0] - susp_cache[i]['garbage_pos'][0]) + abs(susp_cache[i - 1]['scooter_pos'][1] - susp_cache[i]['garbage_pos'][1]))
    #尋找兩次垃圾和機車很近的距離差異超過THRESHOLD_DISTANCE的frame
    for i in range(1, len(sum_diff)):
        if (sum_diff[i] - sum_diff[i - 1]) > THRESHOLD_DISTANCE:
            print('detected littering at frame:', susp_cache[i]['frame_num'])


def detect_position_in_frame(frame_num, bbox_garbage, bbox_scooter, susp_cache):
    
    for bbox_0 in bbox_garbage[frame_num]:
        x_garbage = bbox_0['center'][0]
        y_garbage = bbox_0['center'][1]

        for bbox_1 in bbox_scooter[frame_num]:
            x_scooter = bbox_1['center'][0]
            y_scooter = bbox_1['center'][1]

        if abs(x_garbage - x_scooter) < THRESHOLD_STARTING and\
              abs(y_garbage - y_scooter) < THRESHOLD_STARTING:
            
            susp_cache.append({
                'frame_num' : frame_num,
                'scooter_pos' : bbox_1['center'],
                'garbage_pos' : bbox_0['center']
            })
        

def convert_class_name(name):
    if name == '0':
        return 'garbage'
    elif name == '1':
        return 'paper'
    elif name == '2':
        return 'plastic'
    elif name == '3':
        return 'scooter'

def get_frame_bbox(bbox, file):
    bbox_local = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            if line[0] != '1':
                bbox_dict = {
                        'class' : convert_class_name(line[0]),
                        'x' : float(line[1]),
                        'y' : float(line[2]),
                        'w' : float(line[3]),
                        'h' : float(line[4]),
                        'center' : (float(line[1]) + float(line[3]) / 2,
                                    float(line[2]) + float(line[4]) / 2)
                    }
                bbox_local.append(bbox_dict)
    bbox.append(bbox_local)
    return bbox

import glob
import cv2
import numpy as np

path_garbage = './exp_garbage/'
path_motor = './exp_motor/'

THRESHOLD_STARTING = 0.15
THRESHOLD_DISTANCE = 0.05

susp_cache = []

if __name__ == '__main__':
    bbox_garbage, bbox_scooter = [], []
    files = glob.glob(path_garbage + 'labels/*.txt')
    for file in files:
        get_frame_bbox(bbox_garbage, file)
    files = glob.glob(path_motor + 'labels/*.txt')
    for file in files:
        #將file中的bbox資訊存進bbox_scooter
        get_frame_bbox(bbox_scooter, file)
    for frame_num in range(min(len(bbox_garbage), len(bbox_scooter))):
        #計算開始丟棄垃圾的畫面是否存在在此frame中
        detect_position_in_frame(int(frame_num), bbox_garbage, bbox_scooter, susp_cache)
    print(susp_cache)
    detect_littering(susp_cache)
