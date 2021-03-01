##################################best logic
import glob
import shutil
import pandas as pd
import cv2
import os


photos = glob.glob(r'*')
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

# for i in name_list:
#     if os.path.exists(i):
#         for j in name_list_image:
#             metadata=j.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', '')
#             if i==metadata:
#                 ppath=i+"/"+j
#                 if not os.path.exists(ppath):
#                     cv2.imwrite(i+"/"+j,cv2.imread(j))
#                     print("image_put")
                
for i in name_list:
    if os.path.exists(i):
        for j in name_list_image:
            metadata=j.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', '')
            if i==metadata:              
                cv2.imwrite(i+"/"+j,cv2.imread(j))
                print("image_put")

        
# C:\Users\saadn\Desktop\subfolder
# metadata = []

# # read image as grey scale
# grey_img = cv2.imread("akhtar_khan_20005608_left.png")
# metadata.append(grey_img)
# # save image
# status = cv2.imwrite('pic/saad.png',metadata[0])

# print("Image written to file-system : ",status)
        
        
        
        
# print(name_list[2])
# print(name_list_image[2])