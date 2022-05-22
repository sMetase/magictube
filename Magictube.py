import pandas as pd
import os

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