################################## For linux
import glob
import shutil
import pandas as pd
import cv2
import os

# Abdul_Reheem_61_left_1527_564_84_89_06122021_060805.jpg
# Imran_Suleman_116__797_462_82_87_06142021_084243



def convertTuple(tup):
    str =  '_'.join(tup)
    return str


photos = glob.glob('/home/saad/Desktop/training_dataset/attendance/*')
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
                x = int(j.split('_')[4])
                y = int(j.split('_')[5])
                w = int(j.split('_')[6])
                h = int(j.split('_')[7])
                # print(j)
                # print(x)
                img = cv2.imread("/home/saad/Desktop/training_dataset/attendance/"+j)
                crop_img = img[y:y+h, x:x+w]
                cv2.imwrite(""+i+"/"+metadata2,crop_img)
                print("image_put")



# img = cv2.imread("/home/saad/Desktop/training_dataset/attendance/Ahmed_Nawaz_7_right_313_315_83_91_06142021_043029.jpg")
# x = 313
# y = 315
# w = 83
# h = 91

# crop_img = img[y:y+h, x:x+w]
# cv2.imwrite("/home/saad/Desktop/training_dataset/Ahmed_Nawaz_7_right_313_315_83_91_06142021_043029.jpg",crop_img)
# cv2.imshow("cropped", crop_img)

# cv2.waitKey(0)