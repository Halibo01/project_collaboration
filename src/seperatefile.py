import pandas
import os
from glob import glob
import shutil
workingpath = r"C:\Users\halil\Desktop\vindir_data\ornek\ornek"
destinationpath = r"C:\Users\halil\Desktop\vindir_data\ornek2"
excelfilepath = r"ornek.xlsx"
excelfile = pandas.read_excel(excelfilepath)
mask = excelfile[['xmin', 'ymin', 'xmax', 'ymax']].isna().any(axis=1)
cleaned_df = excelfile[~mask]

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
            liste = i.path.split("\\")
            yield i.path, i.name[:i.name.index(".")], liste[-2]
        elif i.is_dir():
            yield from dir_scan(i.path)

lenght = len(cleaned_df["image_id"])
previousname = str()
islem = 0
for i in range(0, lenght):
    imagename = cleaned_df["image_id"][i]
    studyid = cleaned_df["study_id"][i]
    if previousname == "" or previousname != imagename:
        previousname = imagename
    elif previousname == imagename:
        islem = printpercentage(i, lenght, islem)
        continue
    destinationfolder = os.path.join(destinationpath, studyid)
    imagelist = glob(workingpath + f"\\*\\{imagename}*.dicom")
    if imagelist == []:
        islem = printpercentage(i, lenght, islem)
        continue
    os.makedirs(destinationfolder, exist_ok=True)
    try:
        shutil.copy2(imagelist[0], destinationfolder)
        islem = printpercentage(i, lenght, islem)
    except:
        islem = printpercentage(i, lenght, islem)
        continue
    
