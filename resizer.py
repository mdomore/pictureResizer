#!/usr/bin/python
# -*- python -*-
# # # -*- coding: utf-8 -*-

'''
Resize pictures and copy to owncloud
'''

import os.path
import glob
from PIL import Image
from resizeimage import resizeimage

#Recursively search for JPG files and get the path to them
for f in glob.glob('./**/*.JPG'):
    name = os.path.basename(f)      #Get the file name
    split = f.split('/')            #Split the complete path in parts

    img = Image.open(f,)             #Open source image
    print('Opening '+f)
    img = resizeimage.resize_thumbnail(img, [1024, 1024])       #Resize the image with a maximum Width or Heigh of 1024
    if os.path.isfile('owncloud/'+split[1]+'/1024_'+name):
        print('Image already exists')
        img.close()
    else:
        print ('Saving new file in owncloud/'+split[1]+'/1024_'+name)
        img.save('owncloud/'+split[1]+'/1024_'+name, img.format)    #Save image to owncloud directory
        img.close()                     #Close source image
