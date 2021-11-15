import os
import collections
from os.path import splitext
from posix import listdir
from pprint import pprint
# We first have to rename the files by giving them unique indices to connect all the structures
directory_path = '/Users/afridshirsekar/Desktop/icet/structure-library-builder/assets/final_structure_dir_cache_1/test_directory'
dir_list = list(range(len(os.listdir(directory_path))))
formula_index ={}
count_xyz = 1
count_cif = 1
for i in dir_list:
    sub_directory_path = os.listdir(directory_path)[i]
    os.chdir(os.path.join(directory_path, sub_directory_path))
    sub_dir_list = list(range(len(os.listdir(os.path.join(directory_path, sub_directory_path)))))
    xyz_list = sorted([i_1 for i_1 in os.listdir() if i_1.split('.')[-1] == 'xyz'])
    cif_list = sorted([i_2 for i_2 in os.listdir() if i_2.split('.')[-1] == 'cif'])
    for  f in  xyz_list:
        [f_name, f_ext] = os.path.splitext(f)
        f_new_name = '{}_{}{}'.format(f_name, count_xyz, f_ext)
        os.rename(f, f_new_name)
        formula_index[count_xyz] = f_name 
        count_xyz += 1
    for  f in cif_list:
        [f_name, f_ext] = os.path.splitext(f)
        f_new_name = '{}_{}{}'.format(f_name, count_cif, f_ext)
        os.rename(f, f_new_name)
        count_cif += 1
#After renaming the files we need to create folders for each structure containing xyz and cif files
    file_mappings = collections.defaultdict()
    for filename in os.listdir():
        file_type = filename.split('.')[0]
        file_mappings.setdefault(file_type,[]).append(filename)
#move files to folder
    for folder_name,folder_items in file_mappings.items():
        folder_path = os.path.join( directory_path, sub_directory_path, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        for folder_items in folder_items:
            source = os.path.join( directory_path, sub_directory_path, folder_items)
            destination = os.path.join(folder_path, folder_items)
            os.rename(source, destination)

