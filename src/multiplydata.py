import os
import cv2
from glob import glob

workingdir = r"C:\Users\halil\Downloads\labels_my-project-name_2023-06-25-08-30-18"
destinationdir = r"C:\Users\halil\Desktop\changed_data"

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def printpercentage(part, whole, previous = None):
    percentagecalc = int(percentage(part, whole))
    if previous == None:
        print(f"işlem %{percentagecalc} oranında tamamlandı")
        return part
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
            yield i.path
        elif i.is_dir():
            yield from dir_scan(i.path)

allfiles = len(glob(workingdir + "\\**.png"))
islem = 0
for n, i in enumerate(dir_scan(workingdir)):
    if not i.endswith(".png"):
        
        continue
    txtname = i.replace(".png", ".txt")
    if not os.path.exists(txtname):
        continue
    islem += 1
    islem = printpercentage(islem, allfiles)
    newpath = i.replace(workingdir, destinationdir)
    newpath = newpath[:-4]
    if os.path.exists(newpath + ".png") and os.path.exists(newpath + ".txt"):
        continue
    image = cv2.imread(i, 0)
    file = open(txtname)
    lines = file.readlines()
    file.close()
    file = open(newpath + ".txt", "w")
    file.writelines(lines)
    file.close
    cv2.imwrite(newpath + ".png", image)
    for k in range(-1, 2):
        flippedimage = cv2.flip(image, k)
        cv2.imwrite(newpath + f"_{k + 2}" + ".png", flippedimage)
        liste = list()
        newlist = list()
        for j in lines:
            liste = j.split(" ")
            liste = [float(m) for m in liste[1:]]
            if k == -1:
                liste[0] = 1 - liste[0]
                liste[1] = 1 - liste[1]
            if k == 0:
                liste[1] = 1 - liste[1]
            if k == 1:
                liste[0] = 1 - liste[0]
            newlist.append(f"{j[0]} {liste[0]} {liste[1]} {liste[2]} {liste[3]}\n")
        newlist[-1] = newlist[-1][:-1]
        file = open(newpath + f"_{k + 2}" + ".txt", "w")
        file.writelines(newlist)
        file.close
            
    
