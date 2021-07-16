################################## For linux
import glob
import shutil
import pandas as pd
import cv2
import os
from distutils.dir_util import copy_tree



path1 = "/home/saad/saad/arcface/insightface/recognition/arcface_torch/aligned_embeddings_omair_shared/register_aligned_cosface50"
# path2 = "/home/saad/saad/arcface/insightface/recognition/arcface_torch/aligned_embeddings_omair_shared/new_registered_cosface50"
dirs1 = os.listdir( path1 )
# dirs2 = os.listdir( path2 )
# print(dirs1[1])

# copy_tree("/home/saad/saad/arcface/insightface/recognition/arcface_torch/aligned_embeddings_omair_shared/new_registered_cosface50/Aqeel_Ahmad_106/", "/home/saad/saad/arcface/insightface/recognition/arcface_torch/aligned_embeddings_omair_shared/new_registered_cosface50/aaaaaaaaaaaaaaaaaaa")

for i in dirs1:
    if not os.path.exists(i): 
        os.makedirs(i)
        copy_tree("/home/saad/saad/arcface/insightface/recognition/arcface_torch/aligned_embeddings_omair_shared/new_registered_cosface50/"+i,"/home/saad/saad/arcface/insightface/recognition/arcface_torch/aligned_embeddings_omair_shared/new_registered_cosface50/same/"+i)
        print("dir")
