
import os
from PIL import Image


path = "/home/salal/saad/preparing_data/train"
obj = os.scandir(path)

for entry in obj:
    if entry.is_dir():
        for x in os.listdir(entry):
            if x.endswith(".png"):
                # print(entry.path)
                split =  x.split(".")[0]
                print(x)
                # print(split)
                im1 = Image.open(entry.path+"/"+x)
                im1.save(entry.path+"/"+split+".jpg")
                os.remove(entry.path+"/"+x)


# it checks images inthe folder which are png and convert them to jpg and delete png images
