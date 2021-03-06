################################## Creating folder from pictures in one folder and puting pictures with agumentation in it.
import glob
import shutil
import pandas as pd
import cv2
import os
import matplotlib.pyplot as plt 
import numpy as np
from scipy import misc, ndimage 
import keras
from keras import backend as K
import imageio
from keras.preprocessing.image import ImageDataGenerator



folder="new"
photos = glob.glob(r"C:/Users/saadn/Desktop/"+folder+"/*")
name_list = [] #folder ka naam
name_list_image = [] #picture ka naam
full_dir = [] #full path of image

for p in photos:
    name_list.append(p.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', ''))
    name_list_image.append(p.split('\\')[-1])
    full_dir.append(p.split('\\')[0])
# print(name_list_image[0])
# print(p)
for i in name_list:
    if not os.path.exists(i): 
        os.makedirs(i)
        print("dir")
#         count=count+1

for m,i in enumerate(name_list):
    if os.path.exists(i):
        for j in name_list_image:
            metadata=j.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', '')
            kk=j.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '')
            kk=kk.split('_.')
            kk=kk[-1]          
            #print(metadata)
            if i==metadata:
                cv2.imwrite(""+i+"/"+j,cv2.imread("C:/Users/saadn/Desktop/"+folder+"/"+j))
                print("image_put")
                
                gen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1,height_shift_range=0.1,shear_range=0.15, zoom_range=0.1,channel_shift_range=10.,horizontal_flip=True)
                image_path =r''+full_dir[m]+'\\'+j
                #obtain image
                image = np.expand_dims(cv2.imread(image_path),0)
                aug_iter=gen.flow(image)
                aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]
                count=0
                for img in aug_images:
                    cv2.imwrite(""+i+"/"+j+""+str(m)+"."+kk,img)
                    print(count)
                    count=count+1
    
                



