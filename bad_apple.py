import cv2 ,time
from PIL import Image
import numpy as np
vidPath="E:\\bad_applevid.mp4"
cap =   cv2.VideoCapture(vidPath)
temp=0
# if cap.isOpened():
#     while True:
#         ret,frame=cap.read()
#         if not ret:
#             print("Cannot receive frame")
#             break
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imwrite(f".\\framepic\\{temp}.jpg",frame)
#         temp+=1
chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]#gray value : high => low 
for i in range(6572):
    img = Image.open(f".\\framePic\\{i}.jpg")
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
    time.sleep(1/60)
