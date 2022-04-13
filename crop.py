import cv2
import os
import shutil

def crop(image):
    # if os.path.exists('cropped'):
    #     shutil.rmtree('cropped')
    # os.mkdir('cropped')

    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    sizeX = img.shape[1]
    sizeY = img.shape[0]

    halfX = round(sizeX / 2)
    halfY = round(sizeY / 2)

    k = 0
    quadrant = 0

    for i in range(0,2):
        for j in range(0,2):
            roi = img[i * halfY:i * halfY + halfY, j * halfX:j * halfX + halfX]
            cv2.imwrite('cropped\image_quad_' + str(k) + ".jpg", roi)
            k += 1
            quadrant += 1

image = 'TEST_FILES/test_case_1.jpg'
crop(image)
