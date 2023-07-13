import os
import shutil
import pandas

def dir_scan(path):
    for i in os.scandir(path):
        if i.is_file():
            yield i.path
        elif i.is_dir():
            yield from dir_scan(i.path)
excelfiledir = r""
workingdir = r"C:\Users\halil\Desktop\vindir_data\ornek3"
destinationdir = r"C:\Users\halil\Desktop\vindir_data\ornek4"
excelfile = pandas.read_excel(excelfiledir)
for i in dir_scan(workingdir):
    if not i.endswith(".png"):
        continue
    imagename = i.split("\\")[-1]
    imagename = imagename[:imagename.index(".")]
    if imagename in excelfile["image_id"]:
        try:
            shutil.copy2(i, destinationdir)
        except:
            ...
    
