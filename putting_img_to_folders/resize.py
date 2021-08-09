from PIL import Image
import os
import PIL
import glob
import cv2

input_img_path = "/home/saad/saad/arcface/traning_dataset/gadoon_factory/gadoon_factory_registered_faces/test_orignal/"
save_path = "/home/saad/saad/arcface/traning_dataset/gadoon_factory/gadoon_factory_registered_faces/orignal_resized/"

def convertTuple(tup):
    str =  '_'.join(tup)
    return str

fixed_height = 1080
photos = glob.glob(input_img_path+"*")

for step, p in enumerate(photos):
    image = Image.open(p)
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)

    str1 = p.split('/')[-1].replace(' ', '').replace('right', '').replace('random', '').replace('left', '').replace('front', '').replace('.jpg', '')
    str2 = str1.split('_')[:3]
    str3 = convertTuple(str2)

    print(str3)
    image.save(save_path+''+str3+'_'+str(step)+'.jpg')