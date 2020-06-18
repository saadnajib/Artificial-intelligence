#import streamlit as st
from keras.preprocessing.image import load_img,img_to_array,array_to_img
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import PIL  
from skimage import color
import matplotlib.pyplot as plt
from glob import glob
from keras.preprocessing import image
from keras.models import Model,load_model
from keras.layers import Conv2D, MaxPooling2D, Activation, BatchNormalization, UpSampling2D, Dropout, Flatten, Dense, Input, LeakyReLU, Conv2DTranspose,AveragePooling2D, Concatenate
from keras.models import load_model
from keras.optimizers import Adam
from keras.models import Sequential
#from tensorflow.compat.v1 import set_random_seed
import numpy as np
import matplotlib.pyplot as plt
import pickle
import requests
from io import BytesIO
import keras.backend.tensorflow_backend as tb
from copy import deepcopy
#import mahotas
# tb._SYMBOLIC_SCOPE.value = True


def model_load(dataset='people2'):
    '''
    Loads the model depending on which dataset we are working on
    '''
    if dataset == 'people1':
        model = load_model('C:/Users/saad najib/Desktop/generator_people_v1.h5')
    if dataset == 'people2':
        model = load_model('C:/Users/saad najib/Desktop/generator_people_v3.h5')
    elif dataset == 'coast':
        model = load_model('C:/Users/saad najib/Desktop/generator_v1.h5')
    return model

def read_img(file, size = (256,256)):
    '''
    reads the images and transforms them to the desired size
    '''
    img = image.load_img(file, target_size=size)
    img = image.img_to_array(img)
    return img


def read_img_url(url, size = (256,256)):
    """
    Read and resize image directly from a url
    """
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((256, 256))
    img = image.img_to_array(img)
    return img

def read_multiple_images(im,dataset='people2'):
    '''
    Read and transforms an image then displays 
    '''
    img = read_img(im).astype('int64')
    l_channel = rgb_to_lab(img,l=True)
    model = model_load(dataset)
    fake_ab = model.predict(l_channel.reshape(1,256,256,1))
    fake = np.dstack((l_channel,fake_ab.reshape(256,256,2)))
    fake = lab_to_rgb(fake).astype('int64')
    multi = np.vstack((img,fake))
    return multi.reshape(2,256,256,3)



def rgb_to_lab(img, l=False, ab=False):
    """
    Takes in RGB channels in range 0-255 and outputs L or AB channels in range -1 to 1
    """
    img = img / 255
    l_chan = color.rgb2lab(img)[:,:,0]
    l_chan = l_chan / 50 - 1
    l_chan = l_chan[...,np.newaxis]

    ab_chan = color.rgb2lab(img)[:,:,1:]
    ab_chan = (ab_chan + 128) / 255 * 2 - 1
    if l:
        return l_chan
    else: 
    	return ab_chan


def lab_to_rgb(img):
    """
    Takes in LAB channels in range -1 to 1 and out puts RGB chanels in range 0-255
    """
    new_img = np.zeros((256,256,3))
    for i in range(len(img)):
        for j in range(len(img[i])):
            pix = img[i,j]
            new_img[i,j] = [(pix[0] + 1) * 50,(pix[1] +1) / 2 * 255 - 128,(pix[2] +1) / 2 * 255 - 128]
    new_img = color.lab2rgb(new_img) * 255
    new_img = new_img.astype('uint8')
    return new_img


def merge_real_fake(image,percentage,dataset):
    '''
    Transforms a photo and displays a percentage of each image merged together
    Percentage depends on slide setting
    '''
    img = read_img(image).astype('int64')
    l_channel = rgb_to_lab(img,l=True)
    model = model_load(dataset)
    fake_ab = model.predict(l_channel.reshape(1,256,256,1))
    fake = np.dstack((l_channel,fake_ab.reshape(256,256,2)))
    fake = lab_to_rgb(fake).astype('int64')
    real = (img*(1.0-percentage)).astype('int64')
    not_real = (fake*percentage).astype('int64')
    if percentage < 0.02:
        return img
    elif percentage > 0.98:
        return fake
    else:
        merged = real+not_real
        return merged

def url_generator(url,dataset='people2'):
    '''
    downloads the image from the url and creates the color channgels, then returns original and created
    '''
    img = read_img_url(url,size=(256,256)).astype('int64')
    l_channel = rgb_to_lab(img,l=True)
    model = model_load(dataset)
    fake_ab = model.predict(l_channel.reshape(1,256,256,1))
    fake = np.dstack((l_channel,fake_ab.reshape(256,256,2)))
    fake = lab_to_rgb(fake).astype('int64')
    return img, fake

def convert_img_size(file_paths):
    '''
    converts all images to 256x256x3
    '''
    all_images_to_array = np.zeros((len(file_paths), 256, 256, 3), dtype='int64')
    for ind, i in enumerate(file_paths):
        img = read_img(i)
        all_images_to_array[ind] = img.astype('int64')
    print('All Images shape: {} size: {:,}'.format(all_images_to_array.shape, all_images_to_array.size))
    return all_images_to_array

def load_images(filepath):
    '''
    Loads in pickle files, specifically the L and AB channels
    '''
    with open(filepath, 'rb') as f:
        return pickle.load(f)
def generator():
        '''
        Creates the generator in Keras
        '''
        model = Sequential()
        
        model.add(Conv2D(64,(3,3),padding='same',strides=2, input_shape=g_image_shape)) #dont need pooling since stride=2 downsizes
        model.add(BatchNormalization())
        model.add(LeakyReLU(0.2))
        #128 x 128
        
        model.add(Conv2D(128, (3,3), padding='same',strides=2))
        model.add(BatchNormalization())
        model.add(LeakyReLU(0.2))
        #64 x 64
        
        model.add(Conv2D(256, (3,3),padding='same',strides=2))
        model.add(BatchNormalization())
        model.add(LeakyReLU(0.2))
        #32 x 32 
        
        model.add(Conv2D(512,(3,3),padding='same',strides=2))
        model.add(BatchNormalization())
        model.add(LeakyReLU(0.2))
        #16 x 16
        
        
        model.add(Conv2DTranspose(256,(3,3), strides=(2,2),padding='same'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        
        model.add(Conv2DTranspose(128,(3,3),strides=(2,2),padding='same'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        
        model.add(Conv2DTranspose(64,(3,3),strides=(2,2),padding='same'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        
        model.add(Conv2DTranspose(32,(3,3),strides=(2,2),padding='same'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        
        model.add(Conv2D(2,(3,3),padding='same'))
        model.add(Activation('tanh'))
        
        l_channel = Input(shape=g_image_shape)
        image = model(l_channel)
        return Model(l_channel,image)


def discriminator():
        '''
        creates a discriminator in keras
        '''
        model = Sequential()
        model.add(Conv2D(32,(3,3), padding='same',strides=2,input_shape=d_image_shape))
        model.add(LeakyReLU(0.2))
        model.add(Dropout(0.25))
        
        model.add(Conv2D(64,(3,3),padding='same',strides=2))
        model.add(BatchNormalization())
        model.add(LeakyReLU(.2))
        model.add(Dropout(0.25))
        
        
        model.add(Conv2D(128,(3,3), padding='same', strides=2))
        model.add(BatchNormalization())
        model.add(LeakyReLU(0.2))
        model.add(Dropout(0.25))
        
        
        model.add(Conv2D(256,(3,3), padding='same',strides=2))
        model.add(BatchNormalization())
        model.add(LeakyReLU(0.2))
        model.add(Dropout(0.25))
        
        
        model.add(Flatten())
        model.add(Dense(1))
        model.add(Activation('sigmoid'))
        
        image = Input(shape=d_image_shape)
        validity = model(image)
        return Model(image,validity)

file_paths = glob('C:/Users/saad najib/Desktop/online classes/dip/Lab Manuals/Lab 03/data sets/img3.jpg')
X_train = convert_img_size(file_paths)
L = np.array([rgb_to_lab(image,l=True)for image in X_train])
AB = np.array([rgb_to_lab(image,ab=True)for image in X_train])    


L_AB_channels = (L,AB)

with open('l_ab_channels.p','wb') as f:
        pickle.dump(L_AB_channels,f)


X_train_L, X_train_AB = load_images('l_ab_channels.p')

g_image_shape = (256,256,1)
d_image_shape = (256,256,2)


#Build the Discriminator
discriminator = discriminator()
discriminator.compile(loss='binary_crossentropy', 
                      optimizer=Adam(lr=0.00008,beta_1=0.5,beta_2=0.999), 
                    metrics=['accuracy']) 
  
#Making the Discriminator untrainable so that the generator can learn from fixed gradient 
discriminator.trainable = False

# Build the Generator 
generator = generator()
  
#Defining the combined model of the Generator and the Discriminator 
l_channel = Input(shape=g_image_shape)
image = generator(l_channel) 
valid = discriminator(image)
  
combined_network = Model(l_channel, valid) 
combined_network.compile(loss='binary_crossentropy', 
                         optimizer=Adam(lr=0.0001,beta_1=0.5,beta_2=0.999))

#loading the model
generator = model_load(dataset='people1')

#print the original image
print(L.shape)
print(AB.shape)
k = lab_to_rgb(np.dstack((L.reshape(256, 256, 1),AB.reshape(256,256,2)))).astype('int64')
img = array_to_img(k)
#mahotas.imsave('orignal.jpg', k)
#img = Image.fromarray(k, 'RGB')
img.save('orignal.jpg')
#img.show()
#print the predicted colored image

pred = generator.predict(X_train_L.reshape(1,256,256,1))
X_train_L = X_train_L.reshape(256,256,1)
print(X_train_L.shape)
print(pred.shape)
x = lab_to_rgb(np.dstack((X_train_L,pred.reshape(256,256,2)))).astype('int64')
print(pred.shape)
img = array_to_img(x)
#mahotas.imsave('output.jpg', x)
#img = Image.fromarray(x, 'RGB')
img.save('output.jpg')
#img.show()