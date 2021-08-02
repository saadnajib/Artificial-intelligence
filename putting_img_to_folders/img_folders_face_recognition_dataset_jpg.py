################################## For linux
import glob
import shutil
import pandas as pd
import cv2
import os
from PIL import Image

# Abdul_Reheem_61_left_1527_564_84_89_06122021_060805.jpg
# Imran_Suleman_116__797_462_82_87_06142021_084243



def convertTuple(tup):
    str =  '_'.join(tup)
    return str


photos = glob.glob('/home/saad/saad/arcface/traning_dataset/gadoon_office/originals_registered_faces/*')
name_list = []
unique_name_list = []
name_list_image = []
for p in photos:
    str1 = p.split('/')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.jpg', '')
    str2 = str1.split('_')[:3]
    str3 = convertTuple(str2)
    # print(str3)
    name_list.append(str3)
    name_list_image.append(p.split('/')[-1])


# print(name_list[0])
# print(name_list_image[0])
# print(len(name_list))
# print(len(name_list_image))

for i in name_list:
    if not os.path.exists(i): 
        os.makedirs(i)
        unique_name_list.append(i)
        print("dir")
#         count=count+1

# print(len(unique_name_list))

# Imran_Suleman_116_random_797_462_82_87_06142021_084243.jpg

for i in unique_name_list:
    if os.path.exists(i):
        count = 0
        for j in name_list_image:
            # metadata1 = j.split('/')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.jpg', '')
            metadata11 = j.split('_')[:3]
            metadata22 = convertTuple(metadata11)
            metadata2 = j.split('/')[-1]          
            if i == metadata22:              
                # print("name    "+metadata22)
                count = count + 1
                # print("i    "+i)
                # print("j   "+j)
                print(count)
                m2 = metadata2.split('.')[0]
                im1 = Image.open("/home/saad/saad/arcface/traning_dataset/gadoon_office/originals_registered_faces/"+j)
                im1.save(""+i+"/"+m2+".jpg")
                print("image_put")



