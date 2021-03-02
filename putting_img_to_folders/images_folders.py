
import glob
import shutil
import pandas as pd
import cv2
import os

#enter your images path here 
photos = glob.glob(r'D:/saad usb/face_recognination_faceNet_triplet_loss/Tess_facenet_code/research-papers/facenet/new/*')
name_list = []
name_list_image = []
for p in photos:
    name_list.append(p.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', ''))
    name_list_image.append(p.split('\\')[-1])
    
for i in name_list:
    if not os.path.exists(i): 
        os.makedirs(i)
        print("dir")
#         count=count+1

for i in name_list:
    if os.path.exists(i):
        
        for j in name_list_image:
            metadata=j.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', '')
            print(metadata)
            if i==metadata:              
                cv2.imwrite(""+i+"/"+j,cv2.imread("D:/saad usb/face_recognination_faceNet_triplet_loss/Tess_facenet_code/research-papers/facenet/new/"+j))
                print("image_put")

