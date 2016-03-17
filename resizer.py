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

extensions = (".jpg",".jpeg",".JPG",".JPEG")

for ext in extensions:
    print(ext)
    #Recursively search for JPG files and get the path to them
    for f in glob.glob('./**/**/*'+ext):
        name = os.path.basename(f)      #Get the file name
        print(os.path.basename(f))
        split = f.split('/')            #Split the complete path in parts
        split2 = split[2].split('-')
        img = Image.open(f,)             #Open source image
        print('Opening '+f)
        img = resizeimage.resize_thumbnail(img, [1024, 1024])       #Resize the image with a maximum Width or Heigh of 1024
        if os.path.isfile('/home/michael/ownCloud/Photos/'+split[1]+'/1024_'+name):
            print('Image already exists')
            img.close()
        else:
            print ('Saving new file in /home/michael/ownCloud/Photos/'+split2[0]+'_'+split2[1]+'/1024_'+name)
            img.save('/home/michael/ownCloud/Photos/'+split2[0]+'_'+split2[1]+'/1024_'+name, img.format)    #Save image to owncloud directory
            img.close()                     #Close source image
        input("Press Enter to continue...")

