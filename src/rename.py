import os

def dir_scan(path):
    for i in os.scandir(path):
        if i.is_file():
            liste = i.path.split("\\")
            yield i.path, i.name[:i.name.index(".")], liste[-2]
        elif i.is_dir():
            yield from dir_scan(i.path)

workingdir = r""
k = 1
for i in dir_scan(workingdir):
    print(k)
    k += 1
    if i.endswith(".dicom.png"):
        newname = i[:-9] + "png"
        os.rename(i, newname)