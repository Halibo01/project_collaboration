import os
from pydicom.pixel_data_handlers.util import apply_voi_lut
import pydicom as pdm
import numpy as np
import cv2

workingpath = r"C:\Users\halil\Desktop\vindir_data\ornek\ornek"

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def printpercentage(part, whole, previous):
    percentagecalc = int(percentage(part, whole))
    if part+1 == whole:
        print("işlem bitti")
        return percentagecalc
    if percentagecalc != previous:
        print(f"işlem %{percentagecalc} oranında tamamlandı")
        return percentagecalc
    else:
        return previous
    
def dir_scan(path):
    for i in os.scandir(path):
        if i.is_file():
            yield i.path  # Dosya yolunu yield ifadesiyle döndürür
        elif i.is_dir():
            yield from dir_scan(i.path)

def makepng2(image_dir):
    dicom = pdm.read_file(image_dir)
    data = apply_voi_lut(dicom.pixel_array, dicom)
    if dicom.PhotometricInterpretation == "MONOCHROME1":
        data = np.amax(data) - data
    data = data - np.min(data)
    data = data / np.max(data)
    data = (data * 255).astype(np.uint8)
    return data

for i in dir_scan(workingpath):
    if not i.endswith(".dicom"):
        continue
    if os.path.exists(i.replace(".dicom", ".png")):
        continue
    image = makepng2(i)
    i = i.replace(".dicom", ".png")
    cv2.imwrite(i, image)

