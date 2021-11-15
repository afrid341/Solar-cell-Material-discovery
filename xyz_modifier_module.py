import os
from collections import defaultdict
import re
from pprint import pprint
import pandas as pd
test_path = '/Users/afridshirsekar/Desktop/icet/structure-library-builder/assets/final_structure_dir_cache_1/failed_structure_list/'


def coord_mapper(test_path):
    os.chdir(test_path)
    file_list = os.listdir()
    dict_index = file_list[0].split('_')[-1].split('.')[0]
    pattern = re.compile('.*xyz')
    xyz_file = list(filter(pattern.match, file_list))

    with open(xyz_file[0], 'r') as f:
        f_contents = f.readlines()
    pass
# pprint(f_contents)

    r = re.compile(r'"\d\.\d*')
    lattice_match = list(r.findall(f_contents[1]))
    lattice_constant = lattice_match[0].strip('"')

    a_max = float(lattice_constant) * 0.75
    a_max = str(a_max)

    r = re.compile(r'\w\w?')
    B_element_match = list(r.findall(f_contents[13]))[0]

    len_file = len(f_contents)
    r_e_c = []

    def coordinates_getter(x):
        r_xyz = re.compile(r'\d\.\d*')
        coord_match = list(r_xyz.findall(x))
        return coord_match
    for i in range(2, 42):
        [x_75, y_75, z_75] = coordinates_getter(f_contents[i])

        r_element = re.compile(r'\w\w?')
        element_match = list(r_element.findall(f_contents[i]))

        if ((x_75 == y_75 == z_75) and (element_match[0] == B_element_match)):
            r_e_c.append(i)

    x_0 = r_e_c[0]
    x_1 = r_e_c[1]

    [x_0rc, y_0rc, z_0rc] = coordinates_getter(f_contents[x_0])
    [x_1rc, y_1rc, z_1rc] = coordinates_getter(f_contents[x_1])

    if x_1rc > x_0rc:
        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if ((x == 0.5) and (y == 0.5) and (z == 0.5)):
                Site1 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)

            if x == 0.5 and y == 0.5 and z == 0.0:
                Site2 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])

            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.5 and y == 0.0 and z == 0.0:
                Site3 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.5 and y == 0.0 and z == 0.5:
                Site4 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.0 and y == 0.5 and z == 0.5:
                Site5 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.0 and y == 0.5 and z == 0.0:
                Site6 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.0 and y == 0.0 and z == 0.0:
                Site7 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.0 and y == 0.0 and z == 0.5:
                Site8 = i

    elif x_0rc == 0:
        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if ((x == 0.25) and (y == 0.25) and (z == 0.25)):
                Site1 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.25 and y == 0.25 and z == 0.75:
                Site2 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.25 and y == 0.75 and z == 0.75:
                Site3 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.25 and y == 0.75 and z == 0.25:
                Site4 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.75 and y == 0.25 and z == 0.25:
                Site5 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.75 and y == 0.25 and z == 0.75:
                Site6 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.75 and y == 0.75 and z == 0.75:
                Site7 = i

        for i in range(2, len(f_contents)):
            [x, y, z] = coordinates_getter(f_contents[i])
            x = float(x)/float(lattice_constant)
            y = float(y)/float(lattice_constant)
            z = float(z)/float(lattice_constant)
            if x == 0.75 and y == 0.75 and z == 0.25:
                Site8 = i

    Sites = [Site1, Site2, Site3, Site4, Site5, Site6, Site7, Site8]

    def element_getter(x):
        r_element = re.compile(r'\w\w?')
        element_match = list(r_element.findall(f_contents[i]))
        return element_match[0]
    a = defaultdict(list)
    for i in Sites:
        a[dict_index].append(element_getter(f_contents[i]))

    return a


os.chdir(test_path)
list_files = os.listdir()
a_list = []
for i in range(len(list_files)):
    parent_directory = (os.path.join(test_path, list_files[i]))
    a_list.append(coord_mapper(parent_directory))

print(a_list[85])
