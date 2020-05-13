import cv2
import os
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
images_dir=os.path.join(BASE_DIR,"images")

face_cascade = cv2.CascadeClassifier(r'C:\Users\saad najib\Desktop\new_python\haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


current_id=0
label_ids={}
x_train=[]
y_labels=[]

for root, dirs,files in os.walk(images_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root,file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            #print(label, path)
            if not label in label_ids:
                label_ids[label]=current_id
                current_id +=1
            id_=label_ids[label]
            #print(label_ids)
            

           # y_labels.append(label)
           # x_train.append(path)
            pil_image = Image.open(path).convert("L")
            size=(550,550)

            final_image= pil_image.resize(size, Image.ANTIALIAS)
            image_array=np.array(final_image,"uint8")
            print(image_array)
            faces = face_cascade.detectMultiScale(image_array, 1.3, 5)

            for (x,y,w,h) in faces:
                roi=image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids,f)
recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")