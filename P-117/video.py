import os
import cv2
path = "Images"
images = []
num = os.listdir(path)
for image in num:
    name , ext = os.path.splitext(image)
    if ext in [".gif",".png",".jpg",".jpeg",".jfif"]:
        file_name = path+"/"+name
        print(file_name)
        images.append(file_name)
print(len(images))

frame = cv2.imread(image[0])
height, width, channels = frame.shape
size = (width,height)
count = len(images)
out = cv2.VideoWriter("video.mp4",cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for i in range(0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done")
