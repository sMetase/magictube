# Magictube.py
# Created by LC
# 2022.5.21

# 引入库
import pandas as pd
import os

path = r"D:\Creep_Recovery" # 定义文件来源
b = -1 # 用于生成文件名
for rootdir, subdir, files in os.walk(path):
    print("\nWe are scanning dic %s" %rootdir)
    b += 1
    savepath = os.path.join(r'C:\Users\Chans\Desktop\Chart','%s.xlsx'%b) #用于定义生成文件位置
    print("The new file will be saved as %s" %savepath)
    file_list = pd.DataFrame()
    for file in files:
        df_txt = pd.read_csv(os.path.join(rootdir,file), skiprows=14, on_bad_lines='skip', sep="\t")
        print("\tWe are scanning file %s" %file)
        df_txt.drop(axis=0, index=0, inplace=True)
        df_txt = df_txt.astype(float)
        file_list = pd.concat([file_list,df_txt])
    file_list.to_excel(savepath, index=False)