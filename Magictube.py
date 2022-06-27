#Magictube.py
#Created by LC
#2022/5/21

import pandas as pd
import os

def merge():
    try:
        path = str(input("Please enter your folder location.\n\t"))
        saveloc = str(input("Please enter the location where you want to save the file.\n\t"))
        x = int(input("Please enter the ending row of the table header\n\t"))
        y = bool(input("Is the first line a unit? 1/0\n\t"))

    except IOError:
        print("Invalid input.")

    else:
        for rootdir, subdir, files in os.walk(path):
            print('\nWe are scanning folder: %s' %rootdir)
            print("The files in this folder are as follows:")
            savepath = os.path.join(saveloc,'%s.xlsx' %rootdir.split("\\")[-1])
            file_list = pd.DataFrame()
            for file in files:
                df_txt = pd.read_csv(os.path.join(rootdir,file), skiprows=x, on_bad_lines='skip', sep="\t") #读取文件
                print("\t%s" %file) #列出文件
                if y: #如果首行是单位则去掉首行
                    df_txt.drop(axis=0, index=0, inplace=True)
                df_txt = df_txt.astype(float)
                file_list = pd.concat([file_list,df_txt])
            if file_list.empty == False:
                file_list.to_excel(savepath, index=False)
                print("These files that mentioned above are merging into one table %s" %savepath)
        print("\nAll done!")

def delete():
    try:
        path = str(input("Please enter your folder location.\n\t"))
        saveloc = str(input("Please enter the location where you want to save the file.\n\t"))
        x = int(input("Please enter the ending row of the table header\n\t"))
    
    except IOError:
        print("Invalid input.")
    
    else:
        for rootdir, subdir, files in os.walk(path):
            print('\nWe are scanning folder: %s' %rootdir)
            print("The files in this folder are as follows:")
            for file in files:
                openpath = os.path.join(path,file)
                savepath = os.path.join(saveloc,file)
                print('\t%s'%file)
                with open(openpath,'r') as f:
                    data = f.readlines()
                    del data[0:x]
                    f_new = open(savepath, 'w')
                    f_new.writelines(data)
                    f_new.close()
            print("These files that mentioned above are processing.")
            print("All done!")

if __name__ == '__main__':
    modes = input("What do you want, merging or deleting? 1/0\n")
    if modes == '1':
        merge()
    elif modes == '0':
        delete()