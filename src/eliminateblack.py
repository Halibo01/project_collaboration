import os
import cv2
import numpy as np
import pandas as pd

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def dir_scan(path):
    for i in os.scandir(path):
        if i.is_file():
            yield i.path
        elif i.is_dir():
            yield from dir_scan(i.path)

workingdir = r"C:\Users\halil\Downloads\labels_my-project-name_2023-06-25-08-30-18"
excelpath = r"C:\Users\halil\Downloads\ornek_2 (2).xlsx"
excelfile = pd.read_excel(excelpath)
namelist = excelfile["image_id"]
filelist = list()
for j in dir_scan(workingdir):
    if j.endswith(".png"):
        filelist.append(j)
pngfilename = [k.split("\\")[-1] for k in filelist]
for m, i in enumerate(namelist):
    if not i + ".png" in pngfilename:
        continue
    xmin = int(excelfile["xmin"][m])
    ymin = int(excelfile["ymin"][m])
    xmax = int(excelfile["xmax"][m])
    ymax = int(excelfile["ymax"][m])
    if xmin < 0:
        xmin = 0
    if ymin < 0:
        ymin = 0
    number = pngfilename.index(i + ".png")
    path = filelist[number]
    image = cv2.imread(path, 0)
    croppedimage = image[ymin:ymax, xmin:xmax]
    treshold = cv2.threshold(croppedimage, 3, 256, cv2.THRESH_BINARY)[-1]
    pixelcount = np.count_nonzero(treshold)
    allpixels = (xmin - xmax) * (ymin - ymax)
    if percentage(pixelcount, allpixels) < 90:
        print(i, "görüntüsü sakıncalı bir görüntü")
    
    
        
        
    
    
        
