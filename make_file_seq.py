#!/usr/bin/python
# ================================
# (C)2020 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# create numbered file copies to make file sequence
# ================================

import os
import shutil
import lx
import modo

max_number = 1829

# choose file to copy
file_source_path = modo.dialogs.fileOpen(ftype='')
directory_path = os.path.dirname(file_source_path)
file_name_only = os.path.splitext(os.path.split(file_source_path)[1])[0]
source_num = int(file_name_only[file_name_only.rfind('_')+1:])
file_name_base = file_name_only[:-5]

print file_source_path
print directory_path
print file_name_only
print source_num
print file_name_base

for i, num in enumerate(range(source_num, max_number), start=source_num+1):
    file_name_numbered = '{}\\{}{:05}.bin'.format(directory_path, file_name_base, i)
    print file_name_numbered
    shutil.copy(file_source_path, file_name_numbered)

