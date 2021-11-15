import re
import os
from typing import Pattern
import pandas as pd
import glob
from ase.io import read, write
import numpy as np

root_folder_path = '/Users/afridshirsekar/Desktop/icet/structure-library-builder/assets/'
os.chdir(root_folder_path)

df_csv = pd.read_csv('structure-walltimes.csv', delim_whitespace= '\s', names=['index','rub','ish', 'walltimes'])
df_rubbish = pd.DataFrame(df_csv)
df = df_rubbish.drop(['rub','ish'], axis=1)

failed_list = []
for i in range(205):
    if df['walltimes'][i][1] == '0':
        failed_list.append(df['index'][i])
     
parent_path = 'final_structure_dir_cache_1/all_structure_list'
parent_directory_path = os.path.join(root_folder_path, parent_path)
os.chdir(parent_directory_path)

sub_directory_list = os.listdir()
len_list = len(sub_directory_list)

failed_list_str =[]  
for i in range(len(failed_list)):
    failed_list_str.append(failed_list[i].astype(str))

pd.DataFrame(failed_list_str).to_csv('failed_list_index.txt')


""" for i in range(len_list):
    if sub_directory_list[i].split('_')[-1]  in failed_list_str:
        source = os.path.join(root_folder_path, 'final_structure_dir_cache_1/all_structure_list','{}'.format(sub_directory_list[i]))
        destination = os.path.join(root_folder_path,'final_structure_dir_cache_1/failed_structure_list','{}'.format(sub_directory_list[i]))
        os.rename(source, destination)
 """

  
""" for i in range(len_list):
    if sub_directory_list[i].split('_')[-1]  in failed_list_str:
        os.chdir(sub_directory_list[i])
        print(os.getcwd())
        filename = sub_directory_list[i]
        readfile = read('{}.cif'.format(filename))
        write('{}.xyz'.format(filename), readfile)
        os.chdir(parent_directory_path)
        """