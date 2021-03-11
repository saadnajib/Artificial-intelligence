################################## pairs created
import glob
import shutil
import pandas as pd
import cv2
import os
import numpy as np 

flag1 = False

photos = glob.glob(r'C:\Users\saadn\Desktop\radykov_facenet\facial-recognition-video-facenet\src\training_data_raw4\*')
name_list = []
# name_list_image = []
for i, p in enumerate(photos):
    name_list.append(p.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', ''))
    # name_list_image.append(p.split('\\')[-1])
    
    if flag1 == False:
        # flag1=True
        my_file = open("pairs_created.txt", "a")
        my_file.write(name_list[i]+"    front   left\n")
        my_file.write(name_list[i]+"    front   right\n")
        my_file.write(name_list[i]+"    front   random\n")
        my_file.write(name_list[i]+"    left    right\n")
        my_file.write(name_list[i]+"    left    random\n")
        my_file.write(name_list[i]+"    right   random\n")
        my_file.close()


for j in range(len(photos)):

    rand = np.random.randint(len(name_list))
    while rand == j:
        rand = j+1

    my_file = open("pairs_created.txt", "a")
    my_file.write(name_list[j]+"    front   "+name_list[rand]+" front\n")
    my_file.write(name_list[j]+"    front   "+name_list[rand]+" left\n")
    my_file.write(name_list[j]+"    front   "+name_list[rand]+" right\n")
    my_file.write(name_list[j]+"    front   "+name_list[rand]+" random\n")

    my_file.write(name_list[j]+"    left    "+name_list[rand]+" front\n")
    my_file.write(name_list[j]+"    left    "+name_list[rand]+" left\n")
    my_file.write(name_list[j]+"    left    "+name_list[rand]+" right\n")
    my_file.write(name_list[j]+"    left    "+name_list[rand]+" random\n")

    my_file.write(name_list[j]+"    right   "+name_list[rand]+" front\n")
    my_file.write(name_list[j]+"    right   "+name_list[rand]+" left\n")
    my_file.write(name_list[j]+"    right   "+name_list[rand]+" right\n")
    my_file.write(name_list[j]+"    right   "+name_list[rand]+" random\n")

    my_file.write(name_list[j]+"    random  "+name_list[rand]+" front\n")
    my_file.write(name_list[j]+"    random  "+name_list[rand]+" left\n")
    my_file.write(name_list[j]+"    random  "+name_list[rand]+" right\n")
    my_file.write(name_list[j]+"    random  "+name_list[rand]+" random\n")

    my_file.close()
        
    
    
    # else:    
    #     my_file = open("pairs_created.txt", "a")
    #     my_file.write("\nMismatch, "+ filename+ ", "+ matched_filename+"")
    #     my_file.close()


# for i in name_list:
#     if not os.path.exists(i): 
#         os.makedirs(i)
#         print("dir")
# #         count=count+1

# for i in name_list:
#     if os.path.exists(i):
        
#         for j in name_list_image:
#             metadata=j.split('\\')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', '')
#             #print(metadata)
#             if i==metadata:              
#                 cv2.imwrite(""+i+"/"+j,cv2.imread("C:/Users/saadn/Desktop/imagestobecopied/"+j))
#                 print("image_put")



