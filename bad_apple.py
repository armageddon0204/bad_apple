import cv2 ,time,os
from PIL import Image
import numpy as np
vidPath="\\bad_apple\\bad_applevid.mp4"
framesPath = "\\bad_apple\\framePic"
def getFrames():
    cap =  cv2.VideoCapture(vidPath)
    
    temp=0
    if cap.isOpened():
        while True:
            ret,frame=cap.read()
            if not ret:
                print("Cannot receive frame")
                break
            cv2.imwrite(f"\\bad_apple\\framepic\\{temp}.jpg",frame)
            temp+=1
def indicate():
    indicateLen = len(os.listdir(framesPath))
    
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]#gray value : high => low 
    for i in range(indicateLen):
        img = Image.open(f"\\bad_apple\\framePic\\{i}.jpg")
        width, height = img.size
        aspect_ratio = height / width
        new_width = 100
        new_height = int(aspect_ratio * new_width * 0.55)
        img = img.resize((new_width, new_height))
        img = img.convert("L")# pixel value
        
        pixels = np.array(img)
        
        #flatten converts multidimension into one dimension
        ascii_pixels = np.array([chars[pixel // 25] for pixel in pixels.flatten()])#255/25=10.2
        
        
        
        #change  height and width of output  to original shape and translate into two dimensional array

        ascii_pixels = ascii_pixels.reshape(new_height, new_width)#(rows,columns)
        
        ascii_image = "\n".join("".join(row) for row in ascii_pixels)
        print(ascii_image)
        time.sleep(1/10)
if not os.path.exists(framesPath):
    os.makedirs(framesPath)
    getFrames()
else:
    indicate()
