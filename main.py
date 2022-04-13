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
reader = easyocr.Reader(['en'],gpu=False)
list1 = []

def main(path):
    #this function will crop out the image into 4 parts such that we will be 
    #able to run the files in parallel
    crop(path)
    path1 = "cropped/image_quad_0.jpg"
    path2 = "cropped/image_quad_1.jpg"
    path3 = "cropped/image_quad_2.jpg"    
    path4 = "cropped/image_quad_3.jpg"

    p1 = threading.Thread(target=ocr_recognition,args=("Thread-1",path1))
    p2 = threading.Thread(target=ocr_recognition,args=("Thread-2",path2))
    p3 = threading.Thread(target=ocr_recognition,args=("Thread-3",path3))
    p4 = threading.Thread(target=ocr_recognition,args=("Thread-4",path4))
    print("**********Multiprocessing Part is Initialized!***************")
    print(" ")
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    #ocr_recognition("Thread-1",path1)

    #multiprocessing part is done 
    print(" ")
    print("**********Multiprocessing Part is Done!***************")
    #sending_temp = []
    sending_temp = Cloning(list1)
    list1.clear()
    res = change_string(sending_temp)
    return res

def ocr_recognition(thread_name,path):
    
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
    time.sleep(1)

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
   

    