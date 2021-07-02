################################## For linux
import glob
import shutil
import pandas as pd
import cv2
import os

#/home/saad/Desktop/training_dataset/attendance/Ahmed_Nawaz_7_right_289_489_108_104_06102021_061847.jpg
# Abdul_Reheem_61_left_1527_564_84_89_06122021_060805.jpg
# Imran_Suleman_116__797_462_82_87_06142021_084243



def convertTuple(tup):
    str =  '_'.join(tup)
    return str


photos = glob.glob('/home/saad/saad/arcface/traning_dataset/gadoon office/attendance_Gadoon_office_24-06-2021/*')
name_list_image = []
for p in photos:
    name_list_image.append(p.split('/')[-1])


count = 0
for j in name_list_image:
    metadata2 = j.split('/')[-1]          
    count = count + 1
    print(count)
    x = int(j.split('_')[4])
    y = int(j.split('_')[5])
    w = int(j.split('_')[6])
    h = int(j.split('_')[7])

    img = cv2.imread("/home/saad/saad/arcface/traning_dataset/gadoon office/attendance_Gadoon_office_24-06-2021/"+j)
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite("/home/saad/saad/arcface/traning_dataset/gadoon office/cropped_faces/"+metadata2,crop_img)
    print("image_put")



