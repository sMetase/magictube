#Rename.py
#Created by LC
#2022/5/21

import os
co = '-'

def rename():
    path = str(input("Please enter your folder location.\n\t"))
    saveloc = str(input("Please enter the location where you want to save the file.\n\t"))
    for rootdir, subdir, files in os.walk(path):
        print("\nWe are scanning folder: %s" %rootdir)
        dirpath = os.path.join(saveloc, rootdir.split('\\')[-1])
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
            print("We created a folder named %s" %dirpath)
        for file in files:
            if file.split(co)[-1][-5] == 'a':
                bename_1 = os.path.join(rootdir,file)
                coname_1 = os.path.join(r'D:\GCreep_Recovery', rootdir.split('\\')[-1],
                file.split('.')[0] + '-001.txt')
                #print(coname_1)
                print("Turning %s\n\tto %s" %(bename_1, coname_1))
                os.rename(bename_1, coname_1)

            else:
                bename_2 = os.path.join(rootdir, file)
                coname_2 = os.path.join(r'D:\GCreep_Recovery',rootdir.split('\\')[-1],
                co.join(file.split(co)[:-1]) +co+ file.split(co)[-1].zfill(7))
                #print(coname_2)
                print("Turing %s\n\tto %s" %(bename_2, coname_2))
                os.rename(bename_2,coname_2)
        
if __name__ == '__main__':
    rename()
    print("All done!")