################################## For linux
import glob
import shutil
import pandas as pd
import cv2
import os


photos = glob.glob('/home/machine-003-001/saad/RajbyCleaned/images/*')
name_list = []
name_list_image = []
for p in photos:
    name_list.append(p.split('/')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', ''))
    name_list_image.append(p.split('/')[-1])

for i in name_list:
    if not os.path.exists(i): 
        os.makedirs(i)
        print("dir")
#         count=count+1

for i in name_list:
    if os.path.exists(i):
        
        for j in name_list_image:
            metadata1=j.split('/')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', '')
            metadata2=j.split('/')[-1].replace(' ', '')
            #print(metadata)
            if i==metadata1:              
                cv2.imwrite(""+i+"/"+metadata2,cv2.imread("/home/machine-003-001/saad/RajbyCleaned/images/"+j))
                print("image_put")


