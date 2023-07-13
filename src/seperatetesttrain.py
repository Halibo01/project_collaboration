import os
import shutil

def dir_scan(path):
    for i in os.scandir(path):
        if i.is_file():
            yield i.path
        elif i.is_dir():
            yield from dir_scan(i.path)
def percentage(part, whole):
  return 100 * float(part)/float(whole)

workingdir = r"C:\Users\halil\Desktop\vindir_data\ornek\ornek"
testdir = r""
traindir = r""
valdir = r""
liste = list()
for i in dir_scan(workingdir):
    if (not i.endswith("TEST.png")) and i.endswith(".png"):
        liste.append(i)
allfiles = len(liste)
for i, j in enumerate(allfiles, start=1):
    if percentage(i, allfiles) <= 80:
        try:
            shutil.copy2(j, traindir)
            shutil.copy2(j.replace(".png", ".txt"), traindir)
        except:
            continue
    elif percentage(i, allfiles) <= 90:
        try:
            shutil.copy2(j, testdir)
            shutil.copy2(j.replace(".png", ".txt"), testdir)
        except:
            continue
    else:
        try:
            shutil.copy2(j, valdir)
            shutil.copy2(j.replace(".png", ".txt"), valdir)
        except:
            continue


