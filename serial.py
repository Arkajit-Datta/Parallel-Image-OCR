import cv2
import os
import shutil
from PIL import Image, ImageEnhance, ImageDraw
import pandas as pd
import numpy as np
from crop import crop
from multiprocessing import Process
import threading
import time
import easyocr
from crop import crop
reader = easyocr.Reader(['en'],gpu=False)
list1 = []

def ocr_recognition_serial(path):
    image = Image.open(path)
    bounds = reader.readtext(np.array(image),decoder = 'beamsearch', beamWidth=10, paragraph = True)
    for i in range(len(bounds)):
        for j in range(len(bounds)-1):
            b = bounds[j][0]
            b1 = bounds[j+1][0]
            if b[0][0]>b1[0][0]:
                temp = bounds[j]
                bounds[j] = bounds[j+1]
                bounds[j+1] = temp
    final_string = str()
    for bound in bounds:
        #print(bound[1])
        final_string += str(bound[1] + ' ')
    print("The recognised part --> "+final_string)
    list1.append(final_string)
    time.sleep(5)
def Cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy

def change_string(list_given):
    res = ""
    temp = 1
    for i in list_given:
        i = str(temp)+" "+i+" "
        res = res+i
        temp = temp+1
    return res

def serial_run(path):
    crop(path)

    #path of the cropped images 
    path1 = r"cropped/image_quad_0.jpg"
    path2 = r"cropped/image_quad_1.jpg"
    path3 = r"cropped/image_quad_2.jpg"    
    path4 = r"cropped/image_quad_3.jpg"

    ocr_recognition_serial(path1)
    ocr_recognition_serial(path2)
    ocr_recognition_serial(path3)
    ocr_recognition_serial(path4)

    sending_temp = Cloning(list1)
    list1.clear()
    res = change_string(sending_temp)
    return res
