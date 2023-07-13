import pydicom as pdm
import pandas as pd
import warnings as ws
import os
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
ws.filterwarnings("ignore")

excelfile = r"C:\Users\halil\Downloads\ornek_2.xlsx"
workingfolder = r"C:\Users\halil\Desktop\vindir_data\ornek\ornek"
excelfile = pd.read_excel(excelfile)



def makerectangle(dicomfile:pdm.Dataset, xmin, ymin, xmax, ymax, thickness = 1):
    dicomimage = dicomfile.pixel_array
    dicomimage[ymin-thickness:ymin+thickness, xmin:xmax] = 2624
    dicomimage[ymin:ymax, xmin-thickness:xmin+thickness] = 2624
    dicomimage[ymax-thickness:ymax+thickness, xmin:xmax] = 2624
    dicomimage[ymin:ymax, xmax-thickness:xmax+thickness] = 2624
    dicomfile.PixelData = dicomimage.tobytes()
    return dicomfile

islem = 0
for i in range(len(excelfile["image_id"])):
    islem = printpercentage(i, len(excelfile), islem)     
    xmax = int(excelfile["xmax"][i])
    xmin = int(excelfile["xmin"][i])
    ymax = int(excelfile["ymax"][i])
    ymin = int(excelfile["ymin"][i])
    imagepath = os.path.join(workingfolder, excelfile["study_id"][i], excelfile["image_id"][i])
    try:
        if os.path.exists(imagepath + "_TEST" + ".dicom"):
            dicomfile = pdm.dcmread(imagepath + "_TEST" + ".dicom")
        else:
            dicomfile = pdm.dcmread(imagepath + ".dicom")
        dicomfile = makerectangle(dicomfile, xmin, ymin, xmax, ymax, 5)
        dicomfile.save_as(imagepath + "_TEST" + ".dicom")
    except:
        continue
