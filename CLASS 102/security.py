import cv2
import dropbox
import time
import random

def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0) 
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = 'image' + str(number) + '.png'
        cv2.imwrite(imageName,frame)
        startTime = time.time
        result = False
    return imageName
    print ("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
takeSnapshot()