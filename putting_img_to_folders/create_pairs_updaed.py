################################## pairs created
import glob
import shutil
import cv2
import os
import numpy as np 

flag1 = False

photos = glob.glob('/home/machine-003-001/saad/facenet-implementation-2/src/num/*')
name_list = []

for i, p in enumerate(photos):
    name_list.append(p.split('/')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.png', ''))

length = len(name_list)
# count = 0
count1 = 0
count2 = 0
flag1 = False
flag2 = False


while(True):
    
    if(flag1==True and flag2==True):
        break

    try:

        for n in range(50):

            my_file = open("pairs_created.txt", "a")
            my_file.write(name_list[count1]+"    front   left\n")
            my_file.write(name_list[count1]+"    front   right\n")
            my_file.write(name_list[count1]+"    front   random\n")
            my_file.write(name_list[count1]+"    left    right\n")
            my_file.write(name_list[count1]+"    left    random\n")
            my_file.write(name_list[count1]+"    right   random\n")
            count1 += 1

    except IndexError as e:
        message = e.args[0]
        print(message)
        flag1=True

    try:

        for j in range(50):

            rand = np.random.randint(len(name_list))
            if rand == count2:
                rand = count2+1

            my_file = open("pairs_created.txt", "a")
            my_file.write(name_list[count2]+"    front   "+name_list[rand]+" front\n")
            my_file.write(name_list[count2]+"    front   "+name_list[rand]+" left\n")
            my_file.write(name_list[count2]+"    left    "+name_list[rand]+" left\n")
            my_file.write(name_list[count2]+"    left    "+name_list[rand]+" right\n")
            my_file.write(name_list[count2]+"    right   "+name_list[rand]+" random\n")
            my_file.write(name_list[count2]+"    random  "+name_list[rand]+" front\n")
            count2 += 1

    except IndexError as e:
        message = e.args[0]
        print(message)
        flag2=True

    # count += 1

my_file.close()
        
    
    