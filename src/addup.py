import os
import shutil

def dir_scan(path):
    for i in os.scandir(path):
        if i.is_file():
            yield i.path  # Dosya yolunu yield ifadesiyle döndürür
        elif i.is_dir():
            yield from dir_scan(i.path)

workingdir = r""
txtfiledir = r"C:\Users\halil\Desktop\vindir_data\ornek\ornek"
namelist = list()
for j in dir_scan(txtfiledir):
    if j.endswith(".dicom"):
        k = j.split("\\")[-1]
        k = k[:k.index(".")]
        namelist.append(k)

print("there are " + str(len(namelist)) + " txt files")

for i in dir_scan(workingdir):
    if i.endswith(".png"):
        k = i.split("\\")[-1]
        k = k[:k.index(".")]
        if k in namelist:
            try:
                shutil.copy2(i, txtfiledir)
            except:
                pass

    

